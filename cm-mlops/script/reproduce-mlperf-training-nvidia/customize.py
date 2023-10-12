from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    conf = env.get('CM_MLPERF_NVIDIA_TRAINING_SYSTEM_CONF_NAME', '')
    if conf == "":
        return {'return':1, 'error': 'Please provide --system_conf_name=<CONF_SOURCE_FILE>'}

    if not conf.endswith(".sh"):
        conf = conf + ".sh"

    if env.get('CM_MLPERF_TRAINING_BENCHMARK', '') == "resnet":
        i['run_script_input']['script_name'] = "run-resnet"

    env['CONFIG_FILE'] = conf
#    print(env)

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
