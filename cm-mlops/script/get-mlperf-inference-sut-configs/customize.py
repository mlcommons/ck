from cmind import utils
import os
import yaml

def preprocess(i):
    env = i['env']
    state = i['state']
    if 'CM_HW_NAME' not in env:
        env['CM_HW_NAME'] = "default"

    backend = env.get('CM_MLPERF_BACKEND', 'default')
    backend_version = "v" + env.get('CM_MLPERF_BACKEND_VERSION', 'default')

    path = i['run_script_input']['path']
    if 'CM_SUT_CONFIG' not in state:
        state['CM_SUT_CONFIG'] = {}

    if 'CM_SUT_NAME' not in env:
        env['CM_SUT_NAME'] = env['CM_HW_NAME'] + "-" + backend + "-" + backend_version

    config_path = os.path.join(path, "configs", env['CM_HW_NAME'], backend, backend_version + "-config.yaml")
    if not os.path.exists(config_path):
        config_path = os.path.join(path, "configs", env['CM_HW_NAME'], backend, "default-config.yaml")
        if not os.path.exists(config_path):
            return {'return':1, "error": "SUT MLC config.yaml not present for system: " + env['CM_HW_NAME'] + " and backend: " + backend}

    state['CM_SUT_CONFIG'][env['CM_SUT_NAME']] = yaml.load(open(config_path), Loader=yaml.SafeLoader)

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
