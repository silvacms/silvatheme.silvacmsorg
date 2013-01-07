
from silvatheme.infraecommon import ITypography
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from silva.core.layout.porto.interfaces import IPorto
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf


class ISilvaCmsOrg(ITypography, IPorto):
    """Layer for SilvaCMS.org theme
    """
    silvaconf.resource('css/silvacmsorg.css')


class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """
    silvaconf.skin('SilvaCMS')


class IAboutResources(IDefaultBrowserLayer, ISilvaCmsOrg):
    pass
