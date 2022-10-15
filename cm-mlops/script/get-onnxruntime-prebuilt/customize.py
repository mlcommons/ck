from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    return {'return':0}

def postprocess(i):

    env = i['env']
    install_folder = env['CM_TMP_INSTALL_FOLDER']
    if '+C_INCLUDE_PATH' not in env: env['+C_INCLUDE_PATH']=[]
    if '+CPLUS_INCLUDE_PATH' not in env: env['+CPLUS_INCLUDE_PATH']=[]
    if '+LD_LIBRARY_PATH' not in env: env['+LD_LIBRARY_PATH']=[]
    if '+DYLD_FALLBACK_LIBRARY_PATH' not in env: env['+DYLD_FALLBACK_LIBRARY_PATH']=[]
    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', install_folder, 'include'))
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', install_folder, 'include'))
    env['+LD_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', install_folder, 'lib'))
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', install_folder, 'lib'))

    return {'return':0}
