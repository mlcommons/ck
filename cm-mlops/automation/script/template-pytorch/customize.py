from cmind import utils
import os

def preprocess(i):

    print ('')
    print ('Preprocessing ...')

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    print ('  ENV CM_VAR1: {}'.format(env.get('CM_VAR1','')))
    
    return {'return':0}

def postprocess(i):

    print ('')
    print ('Postprocessing ...')

    env = i['env']

    return {'return':0}
