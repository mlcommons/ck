from cmind import utils
import os
from os.path import exists
import shutil
import glob

def preprocess(i):

    env = i['env']
    if 'CM_IMAGENET_PREPROCESSED_PATH' in env:
        files = glob.glob(env['CM_IMAGENET_PREPROCESSED_PATH']+"/**/"+env['CM_IMAGENET_PREPROCESSED_FILENAME'], recursive = True)
        if files:
            env['CM_DATASET_PREPROCESSED_PATH'] = env['CM_IMAGENET_PREPROCESSED_PATH']
        else:
            return {'return': 1, 'error': 'No preprocessed images found in '+env['CM_IMAGENET_PREPROCESSED_PATH']}
    else:
        print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

        if 'CM_DATASET_PREPROCESSED_PATH' not in env:
            env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()
        if not exists(os.path.join(env['CM_DATASET_PATH'], "val_map.txt")):
            shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), os.path.join(env['CM_DATASET_PATH'],
            "val_map.txt"))

    if not exists(os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "val_map.txt")):
        shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), os.path.join(env['CM_DATASET_PREPROCESSED_PATH'],
        "val_map.txt"))

    return {'return': 0}
