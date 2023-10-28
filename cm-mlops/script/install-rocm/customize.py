from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    installed_path = "/opt/rocm/bin"
    env['CM_ROCM_INSTALLED_PATH'] = installed_path
    env['CM_ROCM_BIN_WITH_PATH'] = os.path.join(installed_path, "rocminfo")
    env['+PATH'] = [ installed_path ]

    return {'return':0}
