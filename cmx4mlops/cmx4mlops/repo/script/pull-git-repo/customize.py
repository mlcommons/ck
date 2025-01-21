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
import shutil


def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if 'CM_GIT_CHECKOUT_PATH' not in env:
        return {'return': 1, 'error': 'CM_GIT_CHECKOUT_PATH is not set'}

    env['CM_GIT_PULL_CMD'] = "git pull --rebase"

    return {'return': 0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return': 0}
