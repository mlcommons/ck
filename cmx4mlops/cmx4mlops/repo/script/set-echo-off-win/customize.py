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

    state = i['state']

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':

        script_prefix = state.get('script_prefix', [])

        s = '@echo off'
        if s not in script_prefix:
            script_prefix.insert(0, s)

        state['script_prefix'] = script_prefix

    # Test to skip next dependency
    # env = i['env']
    # env['CM_SKIP_SYS_UTILS'] = 'YES'

    return {'return': 0}
