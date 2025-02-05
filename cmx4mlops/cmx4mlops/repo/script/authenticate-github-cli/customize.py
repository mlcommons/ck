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

    cmd = "gh auth login"
    if env.get('CM_GH_AUTH_TOKEN', '') != '':
        if os_info['platform'] == 'windows':
            with open("token", "w") as f:
                f.write(env['CM_GH_AUTH_TOKEN'])
            cmd = f"{cmd} --with-token < token"
        else:
            cmd = f" echo {env['CM_GH_AUTH_TOKEN']} | {cmd} --with-token"

    env['CM_RUN_CMD'] = cmd
    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
