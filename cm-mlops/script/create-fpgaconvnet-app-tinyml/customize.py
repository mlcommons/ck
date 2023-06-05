from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    network_env_name = env['CM_TINY_FPGACONVNET_NETWORK_ENV_NAME']
    run_dir = env['CM_TINY_FPGACONVNET_'+network_env_name+'_RUN_DIR']

    run_cmd = "cd " + run_dir + " && xsct create_boot_image.tcl"

    env['CM_RUN_CMD'] = run_cmd
    env['CM_RUN_DIR'] = run_dir

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':1}

    network = env['CM_TINY_NETWORK_NAME']
    json_location = os.path.join(env['CM_RUN_DIR'], env['CM_TINY_NETWORK_NAME'] + ".json")
    if os.path.exists(json_location):
        print(f"JSON configuration file for {network} created at {json_location}")
    else:
        return {'return':1, 'error': "JSON configuration file generation failed"}
        
    return {'return':0}
