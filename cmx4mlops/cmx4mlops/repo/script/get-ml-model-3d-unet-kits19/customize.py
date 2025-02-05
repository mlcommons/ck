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

    automation = i['automation']

    cm = automation.cmind

    path = os.path.dirname(env['CM_ML_MODEL_FILE_WITH_PATH'])

    if env.get("CM_DAE_EXTRACT_DOWNLOADED", " ") != " ":
        env['CM_ML_MODEL_PATH'] = os.path.join(path, env['CM_ML_MODEL_FILE'])
        env['CM_ML_MODEL_FILE_WITH_PATH'] = env['CM_ML_MODEL_PATH']
    else:
        env['CM_ML_MODEL_PATH'] = path

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_PATH']

    return {'return': 0}
