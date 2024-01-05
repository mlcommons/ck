from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    return {'return': 0}

def postprocess(i):
    env = i['env']
    env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'annotations')

    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH_ROOT'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        annotations_file_path = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-mlperf.json")
        env['CM_DATASET_VALIDATION_ANNOTATIONS_FILE_PATH'] = annotations_file_path
        env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = annotations_file_path
        if env.get("CM_DATASET_OPENIMAGES_CUSTOM_ANNOTATIONS",'') == "yes":
            annotations_file_src = env['CM_DATASET_OPENIMAGES_ANNOTATIONS_FILE_PATH']
            shutil.copy(annotations_file_src, env['CM_DATASET_ANNOTATIONS_DIR_PATH'])
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')
        annotations_file_path = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-calibration-mlperf.json")
        env['CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH'] = annotations_file_path


    return {'return': 0}
