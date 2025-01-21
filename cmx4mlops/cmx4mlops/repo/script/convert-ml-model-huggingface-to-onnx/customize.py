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

    if env.get("CM_MODEL_HUGG_PATH", "") == "":
        return {'return': 1, 'error': 'CM_MODEL_HUGG_PATH is not set'}

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    return {'return': 0}


def postprocess(i):
    os_info = i['os_info']

    env = i['env']
    env['HUGGINGFACE_ONNX_FILE_PATH'] = os.path.join(os.getcwd(), "model.onnx")
    return {'return': 0}
