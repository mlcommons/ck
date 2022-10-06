from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    env['CM_LIB_DNNL_INSTALL_DIR'] = os.getcwd()
    env['+C_INCLUDE_PATH']=[]
    env['+CXX_INCLUDE_PATH']=[]
    env['+LD_LIBRARY_PATH']=[]
    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+CXX_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+LD_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))

    return {'return':0}
