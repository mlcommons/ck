from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    #env['CM_GIT_CHECKOUT'] = env['CM_TMP_GIT_BRANCH_NAME']

    return {'return':0}

def postprocess(i):

    env = i['env']

    paths = [
            "+C_INCLUDE_PATH",
            "+CPLUS_INCLUDE_PATH",
            "+LD_LIBRARY_PATH",
            "+DYLD_FALLBACK_LIBRARY_PATH"
            ]

    for key in paths:
        env[key] = []

    include_paths = [ env['CM_TMP_CURRENT_SCRIPT_PATH'] ]

    for inc_path in include_paths:
        env['+C_INCLUDE_PATH'].append(inc_path)
        env['+CPLUS_INCLUDE_PATH'].append(inc_path)

    version = "master"
    env['CM_QAIC_API_SRC_FILE'] = os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], version, "QAicInfApi.cpp")
    env['CM_QAIC_API_INC_FILE'] = os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], version, "QAicInfApi.h")

    return {'return':0}
