from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    code_path = os.path.join(env['CM_GIT_REPO_CHECKOUT_PATH'], "closed", "fpgaconvnet", "code")
    network_env_name = env['CM_TINY_NETWORK_NAME'].replace("-", "_").upper()
    env['CM_TINY_FPGACONVNET_NETWORK_ENV_NAME'] = network_env_name
    env['CM_TINY_FPGACONVNET_' + network_env_name + '_CODE_PATH'] = code_path

    board = env.get('CM_TINY_BOARD', 'zc706')

    benchmark = env.get('CM_TINY_BENCHMARK', 'ic')

    run_dir = os.path.join(code_path, board, benchmark)
    env['CM_TINY_FPGACONVNET_' + network_env_name + '_RUN_DIR'] = run_dir

    run_cmd = "cd " + run_dir + " && " + env['CM_PYTHON_BIN_WITH_PATH'] + " " + "create_config.py"

    env['ML_MODEL_FILE_WITH_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']
    env['CM_RUN_CMD'] = run_cmd
    env['CM_RUN_DIR'] = run_dir

    return {'return':0}

def postprocess(i):

    env = i['env']

    network = env['CM_TINY_NETWORK_NAME']
    env['CM_TINY_FPGACONVNET_NETWORK_NAME'] = network
    network_env_name = env['CM_TINY_FPGACONVNET_NETWORK_ENV_NAME']

    json_location = os.path.join(env['CM_RUN_DIR'], env['CM_TINY_NETWORK_NAME'] + ".json")
    if os.path.exists(json_location):
        print(f"JSON configuration file for {network} created at {json_location}")
    else:
        return {'return':1, 'error': "JSON configuration file generation failed"}

    env['CM_TINY_FPGACONVNET_CONFIG_FILE_' + network_env_name + '_PATH'] = json_location
    env['CM_GET_DEPENDENT_CACHED_PATH'] = json_location
        
    return {'return':0}
