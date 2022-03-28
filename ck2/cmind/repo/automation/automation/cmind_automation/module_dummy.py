import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    OS automation actions
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, module_name)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
           (artifact) (str) - repository name
           
        """

        print (i)

        return {'return':0}
