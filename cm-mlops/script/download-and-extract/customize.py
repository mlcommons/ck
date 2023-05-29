from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']

    filepath = env['CM_EXTRACT_EXTRACTED_PATH']

    if not os.path.exists(filepath):
        return {'return':1, 'error': 'No extracted path set in "CM_EXTRACT_EXTRACTED_PATH"'}


    if env.get('CM_DAE_FINAL_ENV_NAME'):
        env['CM_DAE_FINAL_ENV_NAME'] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
