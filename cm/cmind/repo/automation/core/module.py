import os

from cmind.automation import Automation
from cmind import utils

# This is just an example of how to import extra files from such a package
# We need to make it unique!
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cm_60cb625a46b38610 import misc

class CAutomation(Automation):
    """
    CM "core" automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)


    ############################################################
    def uid(self, i):
        """
        Generate CM UID.

        Args:
          (CM input dict): empty dict

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * uid (str): CM UID
        """

        return misc.uid(i)
