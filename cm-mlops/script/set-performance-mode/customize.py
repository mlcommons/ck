from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    env['OMP_PROC_BIND'] = 'true'

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
