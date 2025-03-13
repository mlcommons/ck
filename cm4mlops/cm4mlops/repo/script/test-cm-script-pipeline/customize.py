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

# Developers: Grigori Fursin

from cmind import utils
import os


def preprocess(i):

    print('')
    print('customize.py: preprocess')
    print('')

    return {'return': 0}


def postprocess(i):

    automation = i['automation']
    run_script_input = i['run_script_input']
    env = i['env']

    print('')
    print('customize.py: postprocess')
    print('')

    r = automation.run_native_script(
        {'run_script_input': run_script_input, 'env': env, 'script_name': 'run2'})
    if r['return'] > 0:
        return r

    return {'return': 0}


def detect_version(i):

    print('')
    print('customize.py: detect_version')
    print('')

    return {'return': 0}
