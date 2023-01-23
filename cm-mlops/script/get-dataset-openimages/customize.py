from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'annotations')
        env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-mlperf.json")
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
