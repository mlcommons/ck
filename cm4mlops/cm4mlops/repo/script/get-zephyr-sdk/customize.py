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
    env = i['env']
    return {'return': 0}


def postprocess(i):

    env = i['env']
    env['ZEPHYR_TOOLCHAIN_VARIANT'] = "zephyr"
    env['ZEPHYR_SDK_INSTALL_DIR'] = os.path.join(
        os.getcwd(), "zephyr-sdk-" + env['CM_ZEPHYR_SDK_VERSION'])

    return {'return': 0}
