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
    if '+PATH' not in env:
        env['+PATH'] = []
    env['+PATH'].append("$HOME/.local/bin")
    return {'return': 0}


def postprocess(i):

    env = i['env']
    env['CM_ZEPHYR_DIR'] = os.path.join(os.getcwd(), "zephyr")

    return {'return': 0}
