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

    env = i['env']

    env_key = env.get('CM_MODEL_ZOO_ENV_KEY', '')

    path_file = env.get('CM_ML_MODEL_FILE_WITH_PATH','')
    if path_file!='':
        path_dir = os.path.dirname(path_file)

        env['CM_ML_MODEL_PATH'] = path_dir

        if env_key!='':
            env['CM_ML_MODEL_'+env_key+'_PATH'] = path_dir

    if env_key!='':
        env['CM_ML_MODEL_'+env_key+'_FILE_WITH_PATH'] = path_dir

    return {'return':0}
