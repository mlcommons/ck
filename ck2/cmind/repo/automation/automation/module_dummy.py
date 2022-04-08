import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    Automation actions
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
           (artifact) (str) - repository name
           
        """

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}
