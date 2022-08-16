from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    env['+C_INCLUDE_PATH'] = [os.path.join(os.getcwd(), 'install', 'include')]
    env['+CXX_INCLUDE_PATH'] = [os.path.join(os.getcwd(), 'install', 'include')]
    env['+LD_LIBRARY_PATH'] = [os.path.join(os.getcwd(), 'install', 'lib')]
    env['+PYTHONPATH'] = [os.path.join(os.getcwd(), 'install', 'python')]

    return {'return':0}
