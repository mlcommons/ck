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
    preprocess_src = os.path.join(
        env['CM_MLPERF_INFERENCE_3DUNET_PATH'],
        'preprocess.py')
    cmd = 'cd ' + env['CM_MLPERF_INFERENCE_3DUNET_PATH'] + \
        ' && ${CM_PYTHON_BIN_WITH_PATH} preprocess.py --raw_data_dir ' + \
        env['CM_DATASET_PATH'] + ' --results_dir ' + \
        os.getcwd() + ' --mode preprocess'
    env['CM_TMP_CMD'] = cmd

    return {'return': 0}


def postprocess(i):
    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()
        env['CM_DATASET_KITS19_PREPROCESSED_PATH'] = env['CM_DATASET_PREPROCESSED_PATH']

    return {'return': 0}
