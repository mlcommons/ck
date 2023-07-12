from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])

    if env.get('CM_ML_MODEL_PRECISION', '') == "fp32":
        env['CM_ML_MODEL_BERT_LARGE_FP32_PATH'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    elif env.get('CM_ML_MODEL_PRECISION', '') == "int8":
        env['CM_ML_MODEL_BERT_LARGE_INT8_PATH'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}

