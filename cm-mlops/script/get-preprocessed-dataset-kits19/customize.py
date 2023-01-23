from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")
    preprocess_src = os.path.join(env['CM_MLPERF_INFERENCE_3DUNET_PATH'], 'preprocess.py')
    cmd = 'cd '+ env['CM_MLPERF_INFERENCE_3DUNET_PATH'] + ' && ${CM_PYTHON_BIN_WITH_PATH} preprocess.py --raw_data_dir ' + env['CM_DATASET_PATH'] + ' --results_dir ' + os.getcwd() + ' --mode preprocess'
    env['CM_TMP_CMD'] = cmd

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    return {'return': 0}
