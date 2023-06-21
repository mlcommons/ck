from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    path = env.get('GPTJ_CHECKPOINT_PATH', '').strip()

    if path == '' or not os.path.exists(path):
        return {'return':1, 'error':'Please rerun the last CM command with --env.GPTJ_CHECKPOINT_PATH={path to the MLPerf GPT-J checkpoint privately shared by Intel}'}

    env = i['env']

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_CHECKPOINT_PATH']
    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}
