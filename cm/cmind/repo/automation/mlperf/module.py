# CMX interface for mlcr

import os

from cmind.automation import Automation
from cmind import utils
from cmind import cli

class CAutomation(Automation):
    """
    CMX interface for mlperf/mlcr
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def for(self, i):
        """
        CMX interface for MLPerf
        
        """

        _cmd = i['control']['_cmd'][2:]

        cmd = 'mlcr ' + ' '.join(_cmd)

        returncode = os.system(cmd)

        r = {'return': returncode}
        if returncode > 0:
            r['error'] = 'mlcr command failed'

        return r
