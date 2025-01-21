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

    env['CM_QAIC_COMPUTE_SDK_PATH'] = env['CM_GIT_CHECKOUT_PATH']

    '''
    if env.get('+PATH', []) == []:
        env['+PATH'] = []
    env['+PATH'].append(env['CM_LLVM_INSTALLED_PATH'])

    if env.get('+LD_LIBRARY_PATH', []) == []:
        env['+LD_LIBRARY_PATH'] = []
    env['+LD_LIBRARY_PATH'].append(os.path.join(env['CM_LLVM_INSTALLED_PATH'], "..", "lib"))
    '''
    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return': 0}


def postprocess(i):

    env = i['env']
    # env['CM_QAIC_RUNNER_PATH'] = os.path.join(env['CM_QAIC_SOFTWARE_KIT_PATH'], "build", "utils", "qaic-runner")

    if '+PATH' not in env:
        env['+PATH'] = []

    env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH'] = os.path.join(
        os.getcwd(),
        "src",
        "install",
        "qaic-compute-" +
        env['CM_QAIC_COMPUTE_SDK_INSTALL_MODE'])

    env['QAIC_COMPUTE_INSTALL_DIR'] = env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH']

    env['+PATH'].append(os.path.join(env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH'], "exec"))

    return {'return': 0}
