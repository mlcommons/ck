# CM wrapper for older CK framework in case it is still needed
#
# Authors: Grigori Fursin
# Contributors:
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import os

from cmind.automation import Automation
from cmind import utils


class CAutomation(Automation):
    """
    CM front-end to the legacy CK framework
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def any(self, i):
        """
        CM filter for CK commands.

        Example:
          cm run ck program:*susan*

        Args:
          (CM input dict): pass to CK

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from the CK automation action

        """

        import ck.kernel as ck

        artifact = i.get('artifact', '')

        i['cid'] = artifact

        if 'out' not in i:
            i['out'] = 'con'

        return ck.access(i)
