from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    env['+PYTHONPATH']=[]
    env['+C_INCLUDE_PATH']=[]
    env['+CPLUS_INCLUDE_PATH']=[]
    env['+LD_LIBRARY_PATH']=[]
    env['+DYLD_FALLBACK_LIBRARY_PATH']=[]
    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+LD_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+PYTHONPATH'].append(os.path.join(os.getcwd(), 'install', 'python'))

    return {'return':0}
