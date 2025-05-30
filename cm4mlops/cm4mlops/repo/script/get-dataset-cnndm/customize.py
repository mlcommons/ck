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

    env = i['env']

    if env.get('CM_CNNDM_INTEL_VARIATION', '') == 'yes':
        i['run_script_input']['script_name'] = "run-intel"
    else:
        print("Using MLCommons Inference source from '" +
              env['CM_MLPERF_INFERENCE_SOURCE'] + "'")

    return {'return': 0}


def postprocess(i):
    env = i['env']

    if env.get('CM_DATASET_CALIBRATION', '') == "no":
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_EVAL_PATH'] = os.path.join(
            os.getcwd(), 'install', 'cnn_eval.json')
        env['CM_DATASET_CNNDM_EVAL_PATH'] = os.path.join(
            os.getcwd(), 'install', 'cnn_eval.json')
        env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_DATASET_PATH']
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(
            os.getcwd(), 'install', 'cnn_dailymail_calibration.json')
        env['CM_CALIBRATION_DATASET_CNNDM_PATH'] = os.path.join(
            os.getcwd(), 'install', 'cnn_dailymail_calibration.json')
        env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_CALIBRATION_DATASET_PATH']

    return {'return': 0}
