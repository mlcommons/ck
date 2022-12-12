from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    return {'return':0}

def postprocess(i):
    env = i['env']
    env['CM_ML_MODEL_ORIGINAL_FILE_WITH_PATH']= env['CM_ML_MODEL_FILE_WITH_PATH']
    env['CM_ML_MODEL_FILE']='model-tvm.so'
    env['CM_ML_MODEL_PATH'] = os.path.join(os.getcwd())
    env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(os.getcwd(), env['CM_ML_MODEL_FILE'])
    env['CM_ML_MODEL_FRAMEWORK'] = "tvm-"+env['CM_ML_MODEL_FRAMEWORK']
    env['CM_ML_MODEL_INPUT_SHAPES'] = env['CM_ML_MODEL_INPUT_SHAPES'].replace("BATCH_SIZE", env['CM_ML_MODEL_MAX_BATCH_SIZE'])

    return {'return':0}
