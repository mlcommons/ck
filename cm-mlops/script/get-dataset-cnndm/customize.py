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
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_EVAL_PATH'] = os.path.join(os.getcwd(), 'install', 'cnn_eval.json')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'cnn_dailymail_calibration.json')

    return {'return': 0}
