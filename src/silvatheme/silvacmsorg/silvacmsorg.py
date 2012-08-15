from zope.cachedescriptors.property import CachedProperty

from silva.app.page.interfaces import IPage
from silva.core.contentlayout import Design, Slot
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf
from silva.core.layout.porto import porto
from silva.core.layout.porto.interfaces import IPorto
from silva.core.interfaces import IPublication

from five import grok


class ISilvaCmsOrg(IPorto):
    """Layer for SilvaCMS.org theme
    """

    silvaconf.resource('css/html5reset.css')
    silvaconf.resource('css/typography.css')
    silvaconf.resource('css/visitorvu.css')
    silvaconf.resource('css/silvacmsorg.css')

    # xxx these should only get registered for about
    silvaconf.resource('slidorion/css/slidorion.css')
    silvaconf.resource('slidorion/js/jquery.min.js')
    silvaconf.resource('slidorion/js/jquery.easing.js')
    silvaconf.resource('slidorion/js/jquery.slidorion.min.js')

class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """

    silvaconf.skin('SilvaCMS')


silvaconf.layer(ISilvaCmsOrg)

class Navigation(porto.Navigation):
    max_depth = 1


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
            return 'active'
        return ''


class Favicon(porto.Favicon):
    """Declare that we have a favicon for this layer.

    Default favicon url is static/favicon.ico so we don't need to
    do anything besides declaring the Favicon viewlet inside this
    layer and have a static/favicon.ico file.
    If you want it to be something different, define a favicon_url property
    or method for this class.
    """
    pass


# class IAboutResources(IDefaultBrowserLayer):
#   silvaconf.resource('slidorion/css/reset.css')
#   silvaconf.resource('slidorion/css/slideorion.css')
#   silvaconf.resource('slidorion/css/style.css')
#   silvaconf.resource('slidorion/js/jquery.min.js')
#   silvaconf.resource('slidorion/js/jquery.easing.js')
#   silvaconf.resource('slidorion/js/jquery.slidorion.min.js')


class About(Design):
   grok.name('about')
   grok.title('About')
   grok.context(IPage)

   slots = {
       'aboutcontent': Slot(css_class='about-content'),
       'screenshots': Slot(css_class='screenshots'),
       'boxfirst': Slot(css_class='box'),
       'boxsecond': Slot(css_class='box'),
       'boxthird': Slot(css_class='box'),
       'morefeatures': Slot(css_class='more-features')}

   def update(self):
       self.title = self.content.get_title_or_id()

