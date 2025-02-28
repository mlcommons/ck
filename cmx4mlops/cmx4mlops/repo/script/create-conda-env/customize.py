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
    run_script_input = i['run_script_input']

    recursion_spaces = i['recursion_spaces']

    if env.get('CM_CONDA_ENV_NAME', '') == '':
        return {'return': 1, 'error': 'Please use "_name.<conda env name>" variation'}

    return {'return': 0}


def postprocess(i):
    env = i['env']

    conda_prefix = os.getcwd()
    env['CONDA_PREFIX'] = conda_prefix
    env['CM_CONDA_PREFIX'] = conda_prefix
    env['CM_CONDA_BIN_PATH'] = os.path.join(conda_prefix, "bin")
    env['CM_CONDA_LIB_PATH'] = os.path.join(conda_prefix, "lib")

    env['+PATH'] = [env['CM_CONDA_BIN_PATH']]
    env['+LD_LIBRARY_PATH'] = [env['CM_CONDA_LIB_PATH']]

    return {'return': 0}
