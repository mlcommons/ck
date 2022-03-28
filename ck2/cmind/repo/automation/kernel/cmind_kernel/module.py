import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    Kernel automation actions
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, module_name)

    ############################################################
    def uid(self, i):
        """
        Generate CM UID
        """

        r = utils.gen_uid()

        if self.cmind.con:
            print (r['uid'])

        return r

