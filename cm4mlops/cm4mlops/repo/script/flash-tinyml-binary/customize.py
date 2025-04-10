#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os


def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}
    if 'CM_TINY_BUILD_DIR' not in env:
        return {
            'return': 1, 'error': 'Please set CM_TINY_BUILD_DIR to the build directory of the model'}
    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
