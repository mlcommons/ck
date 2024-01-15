from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    import json
    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    ml_model = env['CM_MODEL']
    backend = env['CM_MLPERF_BACKEND']
    device = env['CM_MLPERF_DEVICE']
    harness_root = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_PATH'], 'closed', 'Intel', 'code', ml_model, backend+"-"+device)
    print(f"Harness Root: {harness_root}")

    env['CM_HARNESS_CODE_ROOT'] = harness_root

    if env.get('CM_MODEL') == "resnet50":
        pass

    elif "bert" in env.get('CM_MODEL'):
        pass
    elif "retinanet" in env.get('CM_MODEL'):
        pass


    script_path = i['run_script_input']['path']
    if env['CM_MODEL'] == "retinanet":
        env['CM_DATASET_LIST'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']



    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLPERF_USER_CONF' not in env:
        env['CM_MLPERF_USER_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "user.conf")

    
    loadgen_mode = env['CM_MLPERF_LOADGEN_MODE']
    env['CONDA_PREFIX'] = env['CM_CONDA_PREFIX']

    if env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "build_harness":
        i['run_script_input']['script_name'] = "build_harness"
        env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH'] = os.path.join(os.getcwd(), "harness", "build", "bert_inference")
        env['DATA_PATH'] = os.path.join(os.getcwd(), "harness", "bert")
    elif env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "run_harness":
        env['MODEL_PATH'] = os.path.dirname(os.path.dirname(env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH']))
        env['DATASET_PATH'] = os.path.dirname(os.path.dirname(env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH']))
        env['CM_RUN_DIR'] = os.getcwd()
        env['CM_RUN_CMD'] = "bash run_harness.sh"

    return {'return':0}

def postprocess(i):

    env = i['env']
    if env.get('CM_MLPERF_README', '') == "yes":
        import cmind as cm
        inp = i['input']
        state = i['state']
        script_tags = inp['tags']
        script_adr = inp.get('add_deps_recursive', inp.get('adr', {}))

        cm_input = {'action': 'run',
                'automation': 'script',
                'tags': script_tags,
                'adr': script_adr,
                'print_deps': True,
                'env': env,
                'quiet': True,
                'silent': True,
                'fake_run': True
                }
        r = cm.access(cm_input)
        if r['return'] > 0:
            return r

        state['mlperf-inference-implementation'] = {}
        state['mlperf-inference-implementation']['print_deps'] = r['new_state']['print_deps']

    return {'return':0}
