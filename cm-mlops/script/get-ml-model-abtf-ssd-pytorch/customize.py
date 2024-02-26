from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if env.get('CM_ML_MODEL_LOCAL', '') == 'yes':
        ml_model = env.get('CM_ML_MODEL_FILENAME', '')
        if ml_model == '':
            return {'return':1, 'error':'_local.{model name.pth} is not specified'}

        if not os.path.isabs(ml_model):
            ml_model = os.path.join(env.get('CM_TMP_CURRENT_PATH',''), ml_model)

        if not os.path.isfile(ml_model):
            return {'return':1, 'error':'ML model {} is not found'.format(ml_model)}

        env['CM_ML_MODEL_FILE_WITH_PATH'] = ml_model
    
    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}

