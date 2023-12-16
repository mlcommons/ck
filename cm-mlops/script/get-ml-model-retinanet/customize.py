from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if env.get('CM_TMP_ML_MODEL_RETINANET_NO_NMS', '') == 'yes':
        i['run_script_input']['script_name'] = "run-no-nms"
        env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(os.getcwd(), "retinanet.onnx")

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    if env.get('CM_ENV_NAME_ML_MODEL_FILE', '') != '':
        env[env['CM_ENV_NAME_ML_MODEL_FILE']] = env['CM_ML_MODEL_FILE_WITH_PATH']

    if env.get("CM_QAIC_PRINT_NODE_PRECISION_INFO", '') == 'yes':
        env['CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH'] = os.path.join(os.getcwd(), 'node-precision-info.yaml')

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}

