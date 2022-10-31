from cmind import utils
import cmind as cm
import os
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    script_dir = i['run_script_input']['path']
    config_dir = os.path.join(script_dir, env.get('CM_TERRAFORM_CONFIG_DIR_NAME', ''))
    env['CM_TERRAFORM_CONFIG_DIR'] = config_dir
    cache_dir = os.getcwd()
    shutil.copy(os.path.join(config_dir, "credentials.sh"), cache_dir)
    shutil.copy(os.path.join(config_dir, "main.tf"), cache_dir)
    env['CM_TERRAFORM_RUN_DIR'] = os.getcwd()

    return {'return': 0}

def postprocess(i):
    env = i['env']

    return {'return': 0}
