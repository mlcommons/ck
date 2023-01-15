from cmind import utils
import os
import yaml
import shutil

def preprocess(i):
    env = i['env']
    state = i['state']
    if 'CM_HW_NAME' not in env:
        env['CM_HW_NAME'] = "default"

    backend = env.get('CM_MLPERF_BACKEND', 'default')
    if 'CM_MLPERF_BACKEND_VERSION' in env:
        backend_version = "v" + env.get('CM_MLPERF_BACKEND_VERSION')
    else:
        backend_version = 'default'

    path = i['run_script_input']['path']
    if 'CM_SUT_CONFIG' not in state:
        state['CM_SUT_CONFIG'] = {}

    if 'CM_SUT_NAME' not in env:
        env['CM_SUT_NAME'] = env['CM_HW_NAME'] + "-" + backend + "-" + backend_version

    config_path = os.path.join(path, "configs", env['CM_HW_NAME'], backend, backend_version + "-config.yaml")
    if not os.path.exists(config_path):
        config_path_default = os.path.join(path, "configs", env['CM_HW_NAME'], backend, "default-config.yaml")
        if os.path.exists(config_path_default):
            shutil.copy(config_path_default, config_path)
        else:
            print(f"Config file missing for given hw_name '{env['CM_HW_NAME']}' and backend '{backend}', copying from default")
            src_config = os.path.join(path, "configs", "default", "config.yaml")
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            shutil.copy(src_config, config_path)
            shutil.copy(src_config, config_path_default)

    state['CM_SUT_CONFIG'][env['CM_SUT_NAME']] = yaml.load(open(config_path), Loader=yaml.SafeLoader)

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
