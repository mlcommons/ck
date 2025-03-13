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

    env = i['env']
    meta = i['meta']

    env['CM_MLPERF_LOGGING_SRC_PATH'] = env['CM_GIT_REPO_CHECKOUT_PATH']

    return {'return': 0}


def postprocess(i):
    env = i['env']

    env['+PYTHONPATH'] = [env['CM_MLPERF_LOGGING_SRC_PATH']]

    return {'return': 0}
