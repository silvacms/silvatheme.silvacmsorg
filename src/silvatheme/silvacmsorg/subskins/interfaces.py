# Copyright (c) 2013 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id: interfaces.py 24837 2013-03-08 09:43:14Z infrae $

from silvatheme.silvacmsorg.interfaces import ISilvaCmsOrg
from silva.core.layout.interfaces import ISilvaSkin

import silva.core.conf as silvaconf


class ISilvaCmsOrgResponsive(ISilvaCmsOrg, ISilvaSkin):
    """Sub skin with responsive changes for community.
    """
    silvaconf.skin("SilvaCmsOrgResponsive")
    silvaconf.resource("responsive.css")
