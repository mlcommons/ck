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
import shutil


def preprocess(i):

    os_info = i['os_info']

    return {'return': 0}


def postprocess(i):

    env = i['env']
    if env.get('CM_VERSION', '') == '':
        env['CM_VERSION'] = "master"

    if env.get('CM_GIT_REPO_CURRENT_HASH', '') != '':
        env['CM_VERSION'] += "-git-" + env['CM_GIT_REPO_CURRENT_HASH']

    return {'return': 0, 'version': env['CM_VERSION']}
