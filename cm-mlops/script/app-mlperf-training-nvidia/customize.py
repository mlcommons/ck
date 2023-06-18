from cmind import utils
import os
import json
import shutil
import subprocess

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    if env.get('CM_MLPERF_POWER','') == "yes":
        power = "yes"
    else:
        power = "no"

    rerun = True if env.get("CM_RERUN","")!='' else False

    if 'CM_MLPERF_MODEL' not in env:
        return {'return': 1, 'error': "Please select a variation specifying the model to run"}


    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_HOST_CPU_TOTAL_CORES']) // \
                    (int(env.get('CM_HOST_CPU_SOCKETS', '1')) * int(env.get('CM_HOST_CPU_TOTAL_CORES', '1'))))
        else:
            env['CM_NUM_THREADS'] = env.get('CM_HOST_CPU_TOTAL_CORES', '1')

    print("Using MLCommons Training source from '" + env['CM_MLPERF_TRAINING_SOURCE'] +"'")


    NUM_THREADS = env['CM_NUM_THREADS']

    if "bert" in env['CM_MLPERF_MODEL']:
        env['CM_RUN_DIR'] = os.path.join(env['CM_GIT_REPO_CHECKOUT_PATH'], "NVIDIA", "benchmarks", "bert", "implementations", "pytorch-22.09")

    if "resnet" in env['CM_MLPERF_MODEL']:
        env['CM_RUN_DIR'] = os.path.join(env['CM_GIT_REPO_CHECKOUT_PATH'], "NVIDIA", "benchmarks", "resnet", "implementations", "mxnet-22.04")

    env['CM_RESULTS_DIR'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
