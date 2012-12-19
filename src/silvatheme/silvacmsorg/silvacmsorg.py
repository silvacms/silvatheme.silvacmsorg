from zope.cachedescriptors.property import CachedProperty
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from silva.app.page.interfaces import IPage
from silva.core.contentlayout import Design, Slot
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf
from silva.core.layout.porto import porto
from silva.core.layout.porto.interfaces import IPorto
from silva.core.interfaces import IPublication
from silva.fanstatic import need

from silvatheme.infraecommon import ITypography

from js.jquery import jquery

from five import grok


class ISilvaCmsOrg(ITypography, IPorto):
    """Layer for SilvaCMS.org theme
    """

    silvaconf.resource('css/html5reset.css')
    silvaconf.resource('css/typography.css')
    silvaconf.resource('css/silvacmsorg.css')


class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """

    silvaconf.skin('SilvaCMS')


silvaconf.layer(ISilvaCmsOrg)


class Navigation(porto.Navigation):
    max_depth = 1


class IAboutResources(IDefaultBrowserLayer, ISilvaCmsOrg):
    pass


class ICommunityResources(IDefaultBrowserLayer, ISilvaCmsOrg):
   silvaconf.resource('css/bootstrap.min.css')
   silvaconf.resource('css/slideshow.css')
   silvaconf.resource('css/community.css')
   silvaconf.resource(jquery)
   silvaconf.resource('js/slideshow.js')
   silvaconf.resource('js/community.js')


class Layout(porto.Layout):

    @CachedProperty
    def publication_title(self):
        return self.context.get_publication().get_title()

    @CachedProperty
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


class CommunityLayout(Layout):
    pass


class Favicon(porto.Favicon):
    """Declare that we have a favicon for this layer.

    Default favicon url is static/favicon.ico so we don't need to
    do anything besides declaring the Favicon viewlet inside this
    layer and have a static/favicon.ico file.
    If you want it to be something different, define a favicon_url property
    or method for this class.
    """
    pass


class Home(Design):
   grok.name('home')
   grok.title('Home')
   grok.context(IPage)

   slots = {
       'homecontent': Slot(css_class='about-content'),
       'screenshots': Slot(css_class='screenshots'),
       'boxfirst': Slot(css_class='box'),
       'boxsecond': Slot(css_class='box'),
       'boxthird': Slot(css_class='box')}

   def update(self):
       self.title = self.content.get_title_or_id()
       need(IAboutResources)


class About(Design):
   grok.name('about')
   grok.title('About')
   grok.context(IPage)

   slots = {
       'aboutcontent': Slot(css_class='about-content'),
       'featurescontent': Slot(css_class='features-content'),
       'involvedcontent': Slot(css_class='involved-content'),
       'somethingcontent': Slot(css_class='something-content'),
       'news': Slot(css_class='silva-news')}

   def update(self):
       self.title = self.content.get_title_or_id()
       need(IAboutResources)


class Support(Design):
   grok.name('support')
   grok.title('Support')
   grok.context(IPage)

   slots = {
       'supportcontent': Slot(css_class='support-content'),
       'introshort': Slot(css_class=''),
       'introsupport': Slot(css_class='support-intro'),
       'boxfirst': Slot(css_class=''),
       'boxsecond': Slot(css_class=''),
       'boxthird': Slot(css_class='')}

   def update(self):
       self.title = self.content.get_title_or_id()


class Download(Design):
   grok.name('download')
   grok.title('Download')
   grok.context(IPage)

   slots = {
       'downloadcontent': Slot(css_class='download-content'),
       'boxfirst': Slot(css_class=''),
       'boxsecond': Slot(css_class=''),
       'boxthird': Slot(css_class=''),
       'releasescontent': Slot(css_class='')}

   def update(self):
       self.title = self.content.get_title_or_id()


class Community(Design):
   grok.name('community')
   grok.title('community')
   grok.context(IPage)

   slots = {
       'contributeboxcontent': Slot(css_class='box'),
       'reportbugsboxcontent': Slot(css_class='box'),
       'silvaircboxcontent': Slot(css_class='box'),
       'screenshots': Slot(css_class='screenshots'),
       'contributecontent': Slot(css_class='contribute-content'),
       'reportbugscontent': Slot(css_class='report-bugs-content'),
       'silvairccontent': Slot(css_class='silva-irc-content'),
       'boxfirst': Slot(css_class='box'),
       'boxsecond': Slot(css_class='box'),
       'boxthird': Slot(css_class='box')}

   def update(self):
       self.title = self.content.get_title_or_id()
       need(ICommunityResources)
