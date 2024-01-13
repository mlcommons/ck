from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    run_cmd=""

    env['CM_RUN_CMD'] = run_cmd
    env['CM_ONEDNN_INSTALLED_PATH'] = os.path.join(os.getcwd(), "onednn")

    if env.get('CM_FOR_INTEL_MLPERF_INFERENCE', '') == "yes":
        i['run_script_input']['script_name'] = "run-intel-mlperf-inference"

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    return {'return':0}
