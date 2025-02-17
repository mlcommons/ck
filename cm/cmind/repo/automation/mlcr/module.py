# CMX interface for legacy CM front-ends (mlc, mlcr, mlcflow)

# Authors: Grigori Fursin
# Contributors:
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import os

from cmind.automation import Automation
from cmind import utils
from cmind import cli

class CAutomation(Automation):
    """
    CMX interface for legacy CM front-ends (mlc, mlcr, mlcflow)
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def run(self, i):
        """
        CMX interface for legacy CM front-ends (mlc, mlcr, mlcflow)
        
        """

        _cmd = i['control']['_cmd'][2:]

        cmd = 'mlcr ' + ' '.join(_cmd)

        print (cmd)

        returncode = os.system(cmd)

        r = {'return': returncode}
        if returncode > 0:
            r['error'] = 'mlcr command failed'

        return r
