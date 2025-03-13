#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import shutil


def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return': 0}

    if 'CM_MODEL' not in env:
        return {
            'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1,
                'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {
            'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    r = get_run_cmd(env['CM_MODEL'], i)
    if r['return'] > 0:
        return r
    run_cmd = r['run_cmd']
    run_dir = r['run_dir']
    print(run_cmd)
    print(run_dir)
    return {'return': 1, 'error': 'Run command needs to be tested!'}


def get_run_cmd(model, i):
    env = i['env']
    if "gptj" in model:
        scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
        device = env['CM_MLPERF_DEVICE']
        mode = env['CM_MLPERF_LOADGEN_MODE']
        outdir = env['CM_MLPERF_OUTPUT_DIR']
        mlperf_conf_path = env['CM_MLPERF_CONF']
        user_conf_path = env['CM_MLPERF_USER_CONF']
        api_server = env.get('CM_MLPERF_INFERENCE_API_SERVER', 'localhost')
        model_path = env['GPTJ_CHECKPOINT_PATH']
        dataset_path = env['CM_DATASET_CNNDM_EVAL_PATH']
        precision = env['CM_MLPERF_MODEL_PRECISION']
        if mode == "accuracy":
            accuracy_string = " --accuracy "
        else:
            accuracy_string = ""

        run_cmd = f"python3 -u main.py --scenario {scenario} --model-path {model_path} --api-server {api_server} --api-model-name gpt-j-cnn --mlperf-conf {mlperf_conf_path} {accuracy_string} --vllm --user-conf {user_conf_path} --dataset-path {dataset_path} --output-log-dir {outdir} --dtype float32 --device {device} "
        submitter = "CTuning"
        run_dir = os.path.join(
            env['CM_MLPERF_INFERENCE_IMPLEMENTATION_REPO'],
            "open",
            submitter,
            "code",
            "gptj-99")

        return {'return': 0, 'run_cmd': run_cmd, 'run_dir': run_dir}


def postprocess(i):

    env = i['env']

    return {'return': 0}
