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
