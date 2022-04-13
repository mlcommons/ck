import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
           (artifact) (str) - artifact alias or UID
           
        """

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}
