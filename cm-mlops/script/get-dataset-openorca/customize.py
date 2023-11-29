from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH_ROOT'] = env['CM_DATASET_OPENORCA_PATH']
        env['CM_DATASET_PATH'] = env['CM_DATASET_OPENORCA_PATH']
        env['CM_DATASET_OPENORCA_PARQUET'] = os.path.join(env['CM_DATASET_OPENORCA_PATH'], '1M-GPT4-Augmented.parquet')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
