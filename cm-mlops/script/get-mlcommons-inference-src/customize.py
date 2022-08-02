from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    env['CM_TMP_CURRENT_SCRIPT_PATH'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_MLC_INFERENCE_SOURCE'] = os.path.join(os.getcwd(), 'inference')
    env['CM_MLC_INFERENCE_VISION_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision', 'classification_and_detection')

    return {'return':0}
