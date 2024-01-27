from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    # Checking conditions
    if env.get('CM_FAIL_WINDOWS','').lower()=='true':
        if os_info['platform'] == 'windows':
            return {'return':1, 'error': 'CM detected fail condition: running on Windows'}


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
