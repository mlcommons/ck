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

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    file_path = env.get("CM_XILINX_SDK_BIN_PATH")
    if not file_path or not os.path.exists(file_path):
        return {'return': 1, 'error': 'FILE_PATH does not exist'}

    bin_folder_path = os.path.dirname(file_path)
    if '+PATH' in env:
        env['+PATH'].append(bin_foler_path)
    else:
        env['+PATH'] = [bin_folder_path]

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
