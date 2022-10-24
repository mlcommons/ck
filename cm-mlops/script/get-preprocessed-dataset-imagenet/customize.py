from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), os.path.join(env['CM_DATASET_PATH'],
        "val_map.txt"))

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    return {'return': 0}
