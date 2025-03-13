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


def postprocess(i):
    env = i['env']

    script_path = env['CM_TMP_CURRENT_SCRIPT_PATH']

    env['CM_DATASET_IMAGENET_HELPER_PATH'] = script_path
    env['+PYTHONPATH'] = [script_path]

    return {'return': 0}
