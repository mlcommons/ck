from cmind import utils
import os

def postprocess(i):
    env = i['env']
    
    script_path = env['CM_TMP_CURRENT_SCRIPT_PATH']
    
    env['CM_DATASET_IMAGENET_HELPER_PATH'] = script_path
    env['+PYTHONPATH'] = [ script_path ]

    return {'return':0}
