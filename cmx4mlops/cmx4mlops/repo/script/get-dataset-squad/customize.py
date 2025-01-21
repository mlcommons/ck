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

    return {'return': 0}


def postprocess(i):
    env = i['env']

    env['CM_DATASET_SQUAD_PATH'] = os.path.dirname(
        env['CM_DATASET_SQUAD_VAL_PATH'])
    env['CM_DATASET_PATH'] = os.path.dirname(env['CM_DATASET_SQUAD_VAL_PATH'])
    # env['CM_DATASET_SQUAD_VAL_PATH'] = os.path.join(os.getcwd(), env['CM_VAL_FILENAME'])

    return {'return': 0}
