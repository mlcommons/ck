from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    run_dir = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "text_to_image", "tools")

    env['CM_RUN_DIR'] = run_dir

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH_ROOT'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        env['CM_DATASET_CAPTIONS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'captions')
        env['CM_DATASET_LATENTS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'latents')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
