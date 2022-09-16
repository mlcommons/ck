from cmind import utils
import os

def preprocess(i):

    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    print("Using MLCommons Inference source from '" + env['CM_MLC_INFERENCE_SOURCE'] +"'")

    return {'return': 0}
