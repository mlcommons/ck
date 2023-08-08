from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['+PATH'] = [ os.path.join(os.path.expanduser('~'),".cargo", "bin") ]

    return {'return':0}
