from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']
 
    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")
    return {'return': 0}

def postprocess(i):
    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
-        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()
    env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "annotations")
    env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-mlperf.json")

    return {'return': 0}
