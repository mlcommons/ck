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

    if env.get('CM_MLPERF_INFERENCE_INTEL_LANGUAGE_MODEL', '') == "yes":
        i['run_script_input']['script_name'] = "run-intel-mlperf-inference-v3_1"
        run_cmd = "CC=clang CXX=clang++ USE_CUDA=OFF python -m pip install -e . "

        env['CM_RUN_CMD'] = run_cmd
    elif env.get('CM_MLPERF_INFERENCE_INTEL_MODEL', '') in ["resnet50", "retinanet"]:
        i['run_script_input']['script_name'] = "run-intel-mlperf-inference-vision"
        run_cmd = f"CC={env['CM_C_COMPILER_WITH_PATH']} CXX={env['CM_CXX_COMPILER_WITH_PATH']} USE_CUDA=OFF python -m pip install -e . "

        env['CM_RUN_CMD'] = run_cmd

    if not env.get('+ CFLAGS', []):
        env['+ CFLAGS'] = []
    if not env.get('+ CXXFLAGS', []):
        env['+ CXXFLAGS'] = []

    env['+ CFLAGS'] += ["-Wno-error=uninitialized",
                        "-Wno-error=maybe-uninitialized", "-fno-strict-aliasing"]
    env['+ CXXFLAGS'] += ["-Wno-error=uninitialized",
                          "-Wno-error=maybe-uninitialized", "-fno-strict-aliasing"]
    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    return {'return': 0}
