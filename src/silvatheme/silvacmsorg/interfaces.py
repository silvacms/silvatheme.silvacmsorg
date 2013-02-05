
from silva.core import conf as silvaconf
from silva.core.layout.interfaces import ISilvaSkin
from silva.core.layout.porto.interfaces import IPorto
from silvatheme.infraecommon import ITypography

from js.jquery import jquery


class ISilvaCmsOrg(ITypography, IPorto):
    """Layer for SilvaCMS.org theme
    """
    silvaconf.resource('css/silvacmsorg.css')
    silvaconf.resource(jquery)
    silvaconf.resource('js/jquery.stickyPanel.min.js')


class ISilvaCmsOrgSkin(ISilvaCmsOrg, ISilvaSkin):
    """Skin for SilvaCMS.org theme
    """
    silvaconf.skin('SilvaCMS')


class ISilvaSilvaOrgWithNavigation(ISilvaCmsOrg):
    pass


class ISilvaCmsOrgSkinWithNavigation(ISilvaSilvaOrgWithNavigation, ISilvaSkin):
    silvaconf.skin('SilvaCMS with navigation')

