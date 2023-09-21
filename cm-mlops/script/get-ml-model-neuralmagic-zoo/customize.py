from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']
    onnx_path = os.path.join(env['CM_ML_MODEL_FILE_WITH_PATH'], "model.onnx")
    if os.path.exists(onnx_path):
        env['CM_MLPERF_CUSTOM_MODEL_PATH'] = onnx_path

    return {'return':0}
