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

    if env.get('CM_TMP_MLPERF_INFERENCE_LOADGEN_INSTALL_FROM_PIP', '') == 'yes':
        i['run_script_input']['script_name'] = "donotrun"

    return {'return': 0}


def postprocess(i):

    os_info = i['os_info']
    env = i['env']

    if env.get('CM_TMP_MLPERF_INFERENCE_LOADGEN_INSTALL_FROM_PIP', '') == 'yes':
        return {'return': 0}

    for key in ['+PYTHONPATH', '+C_INCLUDE_PATH', '+CPLUS_INCLUDE_PATH',
                '+LD_LIBRARY_PATH', '+DYLD_FALLBACK_LIBRARY_PATH']:
        #        20221024: we save and restore env in the main script and can clean env here for determinism
        #        if key not in env:
        env[key] = []

    # On Windows installs directly into Python distro for simplicity
#    if os_info['platform'] != 'windows':

    cur_path = os.getcwd()
    install_path = os.path.join(cur_path, 'install')

    env['CM_MLPERF_INFERENCE_LOADGEN_INSTALL_PATH'] = install_path

    build_path = os.path.join(cur_path, 'build')
    if os.path.exists(build_path):
        env['CM_MLPERF_INFERENCE_LOADGEN_BUILD_PATH'] = build_path

    include_path = os.path.join(install_path, 'include')
    lib_path = os.path.join(install_path, 'lib')
    python_path = os.path.join(install_path, 'python')

    env['+C_INCLUDE_PATH'].append(include_path)
    env['+CPLUS_INCLUDE_PATH'].append(include_path)
    env['CM_MLPERF_INFERENCE_LOADGEN_INCLUDE_PATH'] = include_path

    env['+LD_LIBRARY_PATH'].append(lib_path)
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(lib_path)
    env['CM_MLPERF_INFERENCE_LOADGEN_LIBRARY_PATH'] = lib_path

    env['+PYTHONPATH'].append(python_path)
    env['CM_MLPERF_INFERENCE_LOADGEN_PYTHON_PATH'] = python_path

    return {'return': 0}
