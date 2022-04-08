import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM front-end to legacy CK framework
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def any(self, i):
        """
        Use as wrapper to CK

        Args:
           (artifact) (str) - repository name
           
        """

        import ck.kernel as ck

        artifact = i.get('artifact','')

        i['cid']=artifact
        
        if 'out' not in i:
           i['out']='con'

        return ck.access(i)
