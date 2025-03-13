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

    env['CC'] = env['CM_C_COMPILER_WITH_PATH']

    return {'return': 0}


def postprocess(i):

    env = i['env']

    for key in ['+C_INCLUDE_PATH', '+CPLUS_INCLUDE_PATH',
                '+LD_LIBRARY_PATH', '+DYLD_FALLBACK_LIBRARY_PATH']:
        #        20221024: we save and restore env in the main script and can clean env here for determinism
        #        if key not in env:
        env[key] = []
    bazel_install_root = os.path.join(os.getcwd(), "src", "bazel-out")
    bazel_install_bin = os.path.join(os.getcwd(), "src", "bazel-bin")
    inc_paths = []
    inc_paths.append(os.path.join(os.getcwd(), "src"))
    inc_paths.append(bazel_install_bin)
    inc_paths.append(
        os.path.join(
            bazel_install_bin,
            "external",
            "flatbuffers",
            "_virtual_includes",
            "flatbuffers"))
    inc_paths.append(
        os.path.join(
            bazel_install_bin,
            "external",
            "FP16",
            "_virtual_includes",
            "FP16"))
    inc_paths.append(
        os.path.join(
            bazel_install_bin,
            "external",
            "pthreadpool",
            "_virtual_includes",
            "pthreadpool"))
    inc_paths.append(
        os.path.join(
            bazel_install_bin,
            "external",
            "cpuinfo",
            "_virtual_includes",
            "cpuinfo"))

    env['+C_INCLUDE_PATH'] = inc_paths
    env['+CPLUS_INCLUDE_PATH'] = inc_paths

    tflite_lib = env.get("CM_TFLITE", "")
    if tflite_lib == "on":
        lib_path = os.path.join(bazel_install_bin, 'tensorflow', 'lite')
    else:
        lib_path = os.path.join(bazel_install_bin, 'tensorflow')
    env['+LD_LIBRARY_PATH'].append(lib_path)
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(lib_path)

    return {'return': 0}
