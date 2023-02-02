from cmind import utils
import os
import yaml
import shutil

def postprocess(i):
    env = i['env']
    state = i['state']

    if env.get('CM_HW_NAME', '') == '':
        host_name =  env.get('CM_HOST_SYSTEM_NAME', 'default')
        env['CM_HW_NAME'] = host_name

    backend = env.get('CM_MLPERF_BACKEND', 'default')
    if env.get('CM_MLPERF_BACKEND_VERSION', '') != '':
        backend_version = "v" + env.get('CM_MLPERF_BACKEND_VERSION') if not env.get('CM_MLPERF_BACKEND_VERSION').startswith("v") else env.get('CM_MLPERF_BACKEND_VERSION')
    else:
        backend_version = 'default'

    if 'CM_SUT_CONFIG' not in state:
        state['CM_SUT_CONFIG'] = {}

    implementation_string = env['CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX'] if env.get('CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX', '') != '' else env.get('CM_MLPERF_IMPLEMENTATION', 'default')
    run_config_string = env['CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX'] if env.get('CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX', '') != '' else 'default'
    if env.get('CM_SUT_NAME', '') == '':
        env['CM_SUT_NAME'] = env['CM_HW_NAME'] + "-" + implementation_string + "-" + backend + "-" + backend_version + "-" + run_config_string

    if env.get('CM_SUT_CONFIGS_PATH',''):
        path = env['CM_SUT_CONFIGS_PATH']
    elif env.get('CM_SUT_USE_EXTERNAL_CONFIG_REPO', '') == "yes":
        path = env.get('CM_GIT_CHECKOUT_PATH')
    else:
        path = os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "configs")

    config_path = os.path.join(path, env['CM_HW_NAME'], implementation_string+"-implementation", backend+"-framework", "framework-version-"+backend_version, run_config_string + "-config.yaml")
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        config_path_default = os.path.join(path, env['CM_HW_NAME'], backend, "default-config.yaml")
        if os.path.exists(config_path_default):
            shutil.copy(config_path_default, config_path)
        else:
            print(f"Config file missing for given hw_name '{env['CM_HW_NAME']}' and backend '{backend}', copying from default")
            src_config = os.path.join(path, "default", "config.yaml")
            shutil.copy(src_config, config_path)
            os.makedirs(os.path.dirname(config_path_default), exist_ok=True)
            shutil.copy(src_config, config_path_default)

    state['CM_SUT_CONFIG'][env['CM_SUT_NAME']] = yaml.load(open(config_path), Loader=yaml.SafeLoader)

    return {'return':0}
