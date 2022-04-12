import os

from cmind.automation import Automation
from cmind import utils

# This is just an example of how to import extra files from such a package
# We need to make it unique!
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cm_60cb625a46b38610 import test

class CAutomation(Automation):
    """
    CM core automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    # Just a test of an import - Grigori moved it to default automation
    def uid(self, i):
        return test.uid(i)
