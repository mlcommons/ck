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

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    run_cmd = "./build.sh --config RelWithDebInfo --build_wheel --parallel --allow_running_as_root --skip_tests "

    if env.get('CM_ONNXRUNTIME_GPU', '') == "yes":
        cuda_home = env['CUDA_HOME']
        run_cmd += f"--use_cuda --cuda_home {cuda_home} --cudnn_home {cuda_home}"

    env['CM_RUN_DIR'] = env['CM_ONNXRUNTIME_SRC_REPO_PATH']
    env['CM_RUN_CMD'] = run_cmd

    return {'return': 0}
