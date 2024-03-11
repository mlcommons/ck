from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    if env.get('CM_MLPERF_INFERENCE_INTEL', '') == "yes":
        i['run_script_input']['script_name'] = "run-intel-mlperf-inference-v3_1"
        run_cmd="CC=clang CXX=clang++ USE_CUDA=OFF python -m pip install -e . "

        env['CM_RUN_CMD'] = run_cmd

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    return {'return':0}

def postprocess(i):
    return {'return':0}
