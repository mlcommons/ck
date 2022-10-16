from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    installed_path = os.path.join(os.getcwd(), 'bin')
    env['CM_TERRAFORM_INSTALLED_PATH'] = installed_path
    env['CM_TERRAFORM_BIN_WITH_PATH'] = os.path.join(installed_path, "terraform")
    env['+PATH'] = [ installed_path ]

    return {'return':0}
