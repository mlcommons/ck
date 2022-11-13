from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']

    for key in ['+PYTHONPATH', '+C_INCLUDE_PATH', '+CPLUS_INCLUDE_PATH', '+LD_LIBRARY_PATH', '+DYLD_FALLBACK_LIBRARY_PATH']:
#        20221024: we save and restore env in the main script and can clean env here for determinism
#        if key not in env:
        env[key] = []

    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+LD_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+PYTHONPATH'].append(os.path.join(os.getcwd(), 'install', 'python'))

    return {'return':0}
