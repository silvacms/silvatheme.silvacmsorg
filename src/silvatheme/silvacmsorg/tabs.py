
import uuid

from five import grok
from grokcore.chameleon.components import ChameleonPageTemplate
from zope.event import notify
from zope.component import queryMultiAdapter
from zope.interface import Interface
from zope.lifecycleevent import ObjectModifiedEvent
from zope.publisher.interfaces.http import IHTTPRequest
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from silva.app.document.interfaces import IDocumentDetails
from silva.core import conf as silvaconf
from silva.core.contentlayout.blocks import Block, BlockController
from silva.core.contentlayout.interfaces import IPage
from silva.core.interfaces import IPublishable
from silva.core.references.reference import Reference
from silva.core.references.reference import ReferenceSet
from silva.translations import translate as _
from silva.fanstatic import need
from zeam.form import silva as silvaforms


class TabBlock(Block):
    grok.name('tab-content')
    grok.title('Tabular content')
    grok.order(21)
    silvaconf.icon('tabs.png')

    def __init__(self):
        self.identifier = unicode(uuid.uuid1())


class ITabResources(IDefaultBrowserLayer):
    silvaconf.resource('js/tabs.js')
    silvaconf.resource('css/tabs.css')


class TabRenderer(object):
    template = ChameleonPageTemplate(filename="tabs.cpt")

    def __init__(self, content, request):
        self.content = content
        self.request = request

    def default_namespace(self):
        return {'request': self.request,
                'view': self}

    def namespace(self):
        return {}

    def update(self):
        need(ITabResources)
        self.tabs = []
        for content in self.content:
            version = content.get_viewable()
            details = queryMultiAdapter(
                (version, self.request), IDocumentDetails)
            if details is None:
                continue
            self.tabs.append(
                {'identifier': uuid.uuid1(),
                 'title': details.get_title(),
                 'content':details.get_text()
                 })

    def __call__(self):
        self.update()
        return self.template.render(self)


class TabBlockController(BlockController):
    grok.adapts(TabBlock, Interface, IHTTPRequest)

    def __init__(self, block, context, request):
        super(TabBlockController, self).__init__(block, context, request)
        self._references = ReferenceSet(self.context, block.identifier)

    def editable(self):
        return True

    @apply
    def content():

        def getter(self):
            return self._references.get()

        def setter(self, value):
            self._references.set(value)

        return property(getter, setter)

    def remove(self):
        self._references.clear()

    def render(self, view=None):
        return TabRenderer(self.content, self.request)()


class ITabFields(Interface):
    content = Reference(
        IPublishable,
        title=u"Content to display in the tabs",
        multiple=True,
        required=True)


class AddTabBlockAction(silvaforms.Action):
    grok.implements(
        silvaforms.IDefaultAction,
        silvaforms.IRESTExtraPayloadProvider,
        silvaforms.IRESTCloseOnSuccessAction)
    title = _('Add')

    def get_extra_payload(self, form):
        adding = form.__parent__
        if adding.block_id is None:
            return {}
        return {
            'block_id': adding.block_id,
            'block_data': adding.block_controller.render(),
            'block_editable': True}

    def __call__(self, form):
        data, errors = form.extractData()
        if errors:
            return silvaforms.FAILURE
        adding = form.__parent__
        adding.add(TabBlock()).content = data['content']
        notify(ObjectModifiedEvent(form.context))
        form.send_message(_(u"New tab component added."))
        return silvaforms.SUCCESS


class AddTabBlock(silvaforms.RESTPopupForm):
     grok.adapts(TabBlock, IPage)
     grok.name('add')

     label = u'Add tabular content'
     fields = silvaforms.Fields(ITabFields)
     actions = silvaforms.Actions(
         silvaforms.CancelAction(),
         AddTabBlockAction())

     def __init__(self, context, request, configuration, restrictions):
         super(AddTabBlock, self).__init__(context, request)
         self.restrictions = restrictions
         self.configuration = configuration


class EditTabBlockAction(silvaforms.Action):
    grok.implements(
        silvaforms.IDefaultAction,
        silvaforms.IRESTExtraPayloadProvider,
        silvaforms.IRESTCloseOnSuccessAction)
    title = _('Save changes')

    def get_extra_payload(self, form):
        # This is kind of an hack, but the name of the form is the block id.
        return {
            'block_id': form.__name__,
            'block_data': form.getContent().render(),
            'block_editable': True}

    def __call__(self, form):
        data, errors = form.extractData()
        if errors:
            return silvaforms.FAILURE
        manager = form.getContentData()
        manager.set('content', data.getWithDefault('content'))
        form.send_message(_(u"Tab component modified."))
        notify(ObjectModifiedEvent(form.context))
        return silvaforms.SUCCESS


class EditTabBlock(silvaforms.RESTPopupForm):
     grok.adapts(TabBlock, IPage)
     grok.name('edit')

     label = u'Edit a slideshow'
     fields = silvaforms.Fields(ITabFields)
     actions = silvaforms.Actions(
         silvaforms.CancelAction(),
         EditTabBlockAction())
     ignoreContent = False

     def __init__(self, block, context, request, controller, restrictions):
         super(EditTabBlock, self).__init__(context, request)
         self.restrictions = restrictions
         self.block = block
         self.setContentData(controller)
