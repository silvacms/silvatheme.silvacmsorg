import datetime

from five import grok
from zope.cachedescriptors.property import Lazy
from zope.traversing.browser import absoluteURL

from silva.core import contentlayout
from silva.core.interfaces import IPublication, IFeedEntryProvider
from silva.core.layout.porto import porto
from silva.core.views import views as silvaviews
from silva.core.contentlayout import Design, Slot

from .interfaces import ISilvaCmsOrg, ISilvaSilvaOrgWithNavigation

grok.templatedir('templates_silvacmsorg')
grok.layer(ISilvaCmsOrg)


class MainLayout(porto.MainLayout):
    grok.template('htmlheadbody')


class Layout(porto.Layout):

    @Lazy
    def publication_title(self):
        return self.context.get_publication().get_title()

    @Lazy
    def publication_url(self):
        return self.context.get_publication().absolute_url()

    def top_menu_items(self):
        root = self.context.get_root()
        def publishable(x):
            return x.is_published() and IPublication.providedBy(x)
        return filter(publishable, root.get_ordered_publishables())

    def current_publication_class(self, publication):
        if publication in self.request.PARENTS:
            return 'selected'
        return ''


class Content(silvaviews.ContentProvider):
    grok.template('content')


class ContentWithNavigation(silvaviews.ContentProvider):
    grok.layer(ISilvaSilvaOrgWithNavigation)
    grok.template('contentwithnavigation')
    grok.name('content')


class Navigation(porto.Navigation):
    max_depth = 1


class Favicon(silvaviews.ContentProvider):
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

    slots = {
        'fullpage': contentlayout.Slot(css_class='content')}

