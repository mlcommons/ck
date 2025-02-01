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

    env['CM_GIT_CHECKOUT'] = "v" + env['CM_VERSION']
    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return': 0}


def postprocess(i):

    env = i['env']
    if '+C_INCLUDE_PATH' not in env:
        env['+C_INCLUDE_PATH'] = []
    if '+LD_LIBRARY_PATH' not in env:
        env['+LD_LIBRARY_PATH'] = []

    gtest_install_path = os.path.join(os.getcwd(), "install")
    env['CM_GOOGLE_TEST_SRC_PATH'] = env['CM_GIT_REPO_CHECKOUT_PATH']
    env['CM_GOOGLE_TEST_INSTALL_PATH'] = gtest_install_path
    env['+C_INCLUDE_PATH'].append(os.path.join(gtest_install_path, "include"))
    env['+LD_LIBRARY_PATH'].append(os.path.join(gtest_install_path, "lib"))

    return {'return': 0}
