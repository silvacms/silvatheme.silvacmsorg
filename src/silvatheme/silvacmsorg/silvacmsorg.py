import datetime

from five import grok
from zope.cachedescriptors.property import Lazy
from zope.traversing.browser import absoluteURL
from zope.component import getUtility

from silva.core import contentlayout
from silva.core.interfaces import IPublication, IRoot, IFeedEntryProvider
from silva.core.layout.porto import porto
from silva.core.services.interfaces import IMetadataService
from silva.core.views import views as silvaviews
from silva.core.layout.interfaces import ICustomizableTag

from .interfaces import ISilvaCmsOrg

grok.templatedir('templates_silvacmsorg')
grok.layer(ISilvaCmsOrg)


class MainLayout(porto.MainLayout):
    grok.template('htmlheadbody')


class INoNavigationLayout(ICustomizableTag):
    """Remove the navigation from the layout
    """


class Layout(porto.Layout):

    @Lazy
    def publication_title(self):
        return self.context.get_publication().get_title()

    @Lazy
    def publication_url(self):
        return self.context.get_publication().absolute_url()

    @Lazy
    def top_menu_items(self):
        root = self.context.get_root()
        get_metadata = getUtility(IMetadataService).getMetadataValue
        is_hidden = lambda c: get_metadata(
            c, 'silva-settings', 'hide_from_tocs', acquire=False) == 'hide'

        def publishable(c):
            return c.is_published() and not is_hidden(c)

        return filter(publishable, root.get_ordered_publishables(IPublication))

    def current_publication_class(self, publication):
        if publication in self.request.PARENTS:
            return 'selected'
        return ''


    def current_section_class(self):
        before = None
        for parent in self.request.PARENTS:
            if IRoot.providedBy(parent):
                if before is not None:
                    return 'section-{0}'.format(before.getId())
                else:
                    break
            before = parent
        return 'section-root'


class ContentNavigationLess(silvaviews.ContentProvider):
    grok.template('contentnavigationless')
    grok.name('content')
    grok.context(INoNavigationLayout)


class ContentWithNavigation(silvaviews.ContentProvider):
    grok.template('contentwithnavigation')
    grok.name('content')


class Navigation(porto.Navigation):
    max_depth = 1


class Favicon(porto.Favicon):
    grok.template('favicon')


class Footer(porto.Footer):
    """Silvacms.org site footer.
    """
    grok.name('footer')

    def get_current_year(self):
        current_year = datetime.datetime.now().year
        return current_year


class HeadInsert(silvaviews.Viewlet):
    """ Custom head insertions
    """
    grok.viewletmanager(porto.HTMLHeadInsert)


class HeadInsertFeeds(silvaviews.Viewlet):
    """Rel link insertions when feeds are active
    """
    grok.viewletmanager(porto.HTMLHeadInsert)

    def update(self):
        feed_provider = IFeedEntryProvider(self.context, None)
        if feed_provider is None:
            container = self.context.get_container()
            self.have_feeds = container.allow_feeds()
            self.feed_url = absoluteURL(container, self.request)
        else:
            if hasattr(self.context, 'allow_feeds'):
                self.have_feeds = self.context.allow_feeds()
            else:
                self.have_feeds = True
            self.feed_url = absoluteURL(self.context, self.request)


class FullPage(contentlayout.Design):
    grok.name('fullpage')
    grok.title('Full Page')

    slots = {'fullpage': contentlayout.Slot(css_class='content')}
    markers = [INoNavigationLayout]

