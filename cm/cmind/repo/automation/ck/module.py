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

        artifact = i.get('artifact','')

        i['cid']=artifact
        
        if 'out' not in i:
           i['out']='con'

        return ck.access(i)
