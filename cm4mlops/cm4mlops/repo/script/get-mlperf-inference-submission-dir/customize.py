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

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '') == '':
        if not os.path.exists("mlperf-inference-submission"):
            os.mkdir("mlperf-inference-submission")
        env['CM_MLPERF_INFERENCE_SUBMISSION_DIR'] = os.path.join(
            os.getcwd(), "mlperf-inference-submission")

    return {'return': 0}


def postprocess(i):

    env = i['env']

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']

    return {'return': 0}
