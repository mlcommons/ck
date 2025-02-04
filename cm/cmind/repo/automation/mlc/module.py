# CMX interface for mlcflow

import os

from cmind.automation import Automation
from cmind import utils
from cmind import cli

class CAutomation(Automation):
    """
    CMX interface for mlcflow
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def run(self, i):
        """
        CMX interface for mlcflow
        
        """

        _cmd = i['control']['_cmd'][2:]

        cmd = 'mlc ' + ' '.join(_cmd)

        returncode = os.system(cmd)

        r = {'return': returncode}
        if returncode > 0:
            r['error'] = 'mlc command failed'

        return r
