from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    if env.get('CM_TVM_PIP_INSTALL', '') == "yes":
        return {'return':0}


    tvm_home = env['TVM_HOME']

#        20221024: we save and restore env in the main script and can clean env here for determinism
#    if '+PYTHONPATH' not in env: env['+PYTHONPATH']=[]
    env['+PYTHONPATH']=[]

    env['+PYTHONPATH'].append(os.path.join(tvm_home,'python'))


    # Prepare paths
    for key in ['+C_INCLUDE_PATH', '+CPLUS_INCLUDE_PATH', '+LD_LIBRARY_PATH', '+DYLD_FALLBACK_LIBRARY_PATH']:
        env[key] = []

    ## Include
    include_path = os.path.join(tvm_home, 'include')
    if os.path.isdir(include_path):
        if os_info['platform'] != 'windows':
            env['+C_INCLUDE_PATH'].append(include_path)
            env['+CPLUS_INCLUDE_PATH'].append(include_path)

        env['CM_TVM_PATH_INCLUDE'] = include_path

    ## Lib
    lib_path = os.path.join(tvm_home, 'build')
    env['+LD_LIBRARY_PATH'].append(lib_path)
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(lib_path)
    env['CM_TVM_PATH_LIB'] = lib_path


    return {'return':0}
