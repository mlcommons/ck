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
import sys


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    utils_path = i['run_script_input']['path']

    env['+PYTHONPATH'] = [utils_path]

    submission_checker_dir = os.path.join(
        env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission")

    sys.path.append(submission_checker_dir)
    sys.path.append(utils_path)

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
