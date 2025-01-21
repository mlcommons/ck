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

    print("Using MLCommons Inference source from '" +
          env['CM_MLPERF_INFERENCE_SOURCE'] + "'")

    run_dir = os.path.join(
        env['CM_MLPERF_INFERENCE_SOURCE'],
        "text_to_image",
        "tools")

    env['CM_RUN_DIR'] = run_dir

    return {'return': 0}


def postprocess(i):
    env = i['env']
    if env.get('CM_GENERATE_SAMPLE_ID', '') == "yes":
        env['CM_COCO2014_SAMPLE_ID_PATH'] = os.path.join(
            os.getcwd(), 'install', 'sample_ids.txt')
        print(env['CM_COCO2014_SAMPLE_ID_PATH'])
    if env.get('CM_DATASET_CALIBRATION', '') == "no":
        env['CM_DATASET_PATH_ROOT'] = os.path.join(os.getcwd(), 'install')
        # env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        env['CM_DATASET_CAPTIONS_DIR_PATH'] = os.path.join(
            os.getcwd(), 'install', 'captions')
        env['CM_DATASET_LATENTS_DIR_PATH'] = os.path.join(
            os.getcwd(), 'install', 'latents')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(
            os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
