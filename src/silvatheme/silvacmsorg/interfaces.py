from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from silva.core import conf as silvaconf
from silva.core.layout.interfaces import ISilvaSkin
from silva.core.layout.porto.interfaces import IPorto

from js.jquery import jquery


class IReset(IDefaultBrowserLayer):
    silvaconf.resource('css/html5reset.css')
    silvaconf.resource('js/modernizr-1.7.min.js')


class ITypography(IReset):
    silvaconf.resource('css/typography.css')


class ISilvaCmsOrg(ITypography, IPorto):
    """Layer for SilvaCMS.org theme
    """
    silvaconf.resource('css/silvacmsorg.css')
    silvaconf.resource(jquery)
    silvaconf.resource('js/jquery.masonry.min.js')
    silvaconf.resource('js/jquery.stickyPanel.min.js')
    silvaconf.resource('js/support.js')


class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """
    silvaconf.skin('SilvaCMS')


class ISilvaSilvaOrgWithNavigation(ISilvaCmsOrg):
    pass


class ISilvaCmsOrgSkinWithNavigation(ISilvaSilvaOrgWithNavigation, ISilvaSkin):
    silvaconf.skin('SilvaCMS with navigation')
