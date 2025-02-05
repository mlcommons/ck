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

    if 'CM_MICROTVM_VARIANT' not in env:
        env['CM_MICROTVM_VARIANT'] = 'microtvm_cmsis_nn'
    if 'CM_TINY_MODEL' not in env:
        env['CM_TINY_MODEL'] = 'ic'

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}
    env['+C_INCLUDE_PATH'] = []
    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
