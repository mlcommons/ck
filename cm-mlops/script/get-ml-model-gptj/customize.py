from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    path = env.get('GPTJ_CHECKPOINT_PATH', '').strip()

    if path == '' or not os.path.exists(path):
        env['CM_TMP_REQUIRE_DOWNLOAD'] = 'yes'

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['GPTJ_CHECKPOINT_PATH'] = os.path.join(env['GPTJ_CHECKPOINT_PATH'], "checkpoint-final")
    env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_CHECKPOINT_PATH']
    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}
