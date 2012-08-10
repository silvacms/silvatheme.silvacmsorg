from zope.cachedescriptors.property import CachedProperty
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf
from silva.core.layout.porto import porto
from silva.core.layout.porto.interfaces import IPorto
from silva.core.interfaces import IPublication


class ISilvaCmsOrg(IPorto):
    """Layer for SilvaCMS.org theme
    """

    silvaconf.resource('css/html5reset.css')
    silvaconf.resource('css/typography.css')
    silvaconf.resource('css/visitorvu.css')
    silvaconf.resource('css/silvacmsorg.css')

class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """

    silvaconf.skin('SilvaCMS')


silvaconf.layer(ISilvaCmsOrg)

class Navigation(porto.Navigation):
    max_depth = 1


class Favicon(porto.Favicon):
    """Declare that we have a favicon for this layer.

    Default favicon url is static/favicon.ico so we don't need to
    do anything besides declaring the Favicon viewlet inside this
    layer and have a static/favicon.ico file.
    If you want it to be something different, define a favicon_url property
    or method for this class.
    """
    pass
