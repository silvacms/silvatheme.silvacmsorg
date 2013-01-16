
from silvatheme.infraecommon import ITypography
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from silva.core.layout.porto.interfaces import IPorto
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf

from js.jquery import jquery

class ISilvaCmsOrg(ITypography, IPorto):
    """Layer for SilvaCMS.org theme
    """
    silvaconf.resource('css/silvacmsorg.css')
    silvaconf.resource(jquery)
    silvaconf.resource('css/slideshow.css')
    silvaconf.resource('js/slideshow.js')


class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """
    silvaconf.skin('SilvaCMS')


class IAboutResources(IDefaultBrowserLayer, ISilvaCmsOrg):
    pass
