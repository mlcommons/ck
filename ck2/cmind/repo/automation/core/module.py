import os

from cmind.module import Module
from cmind import utils

# This is just an example of how to import extra files from such a package
# We need to make it unique!
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cm_60cb625a46b38610 import test

class CModule(Module):
    """
    CM core automation actions
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, __file__)

    ############################################################
    def uid(self, i):
        return test.uid(i, self.cmind.con)
