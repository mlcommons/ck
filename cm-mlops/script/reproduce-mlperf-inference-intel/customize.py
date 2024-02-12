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
    elif "gptj" in env.get('CM_MODEL'):
        env['CHECKPOINT_DIR'] = env['GPTJ_CHECKPOINT_PATH']

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
        if "bert" in env['CM_MODEL']:
            i['run_script_input']['script_name'] = "build_bert_harness"
            env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH'] = os.path.join(os.getcwd(), "harness", "build", "bert_inference")
            env['DATA_PATH'] = os.path.join(os.getcwd(), "harness", "bert")
        elif "gpt" in env['CM_MODEL']:
            i['run_script_input']['script_name'] = "build_gptj_harness"
            env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH'] = os.path.join(os.getcwd(), "harness", "build", "gptj_inference")
            env['DATA_PATH'] = os.path.join(os.getcwd(), "harness", "gptj")
            env['MLPERF_INFERENCE_ROOT'] = env['CM_MLPERF_INFERENCE_SOURCE']
            final_model_path = os.path.join(harness_root, "data", "gpt-j-int8-model")
            env['INT8_MODEL_DIR'] = os.path.dirname(final_model_path)
            env['CM_ML_MODEL_PATH'] = final_model_path

    elif env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "run_harness":
        if env.get('CM_MLPERF_LOADGEN_MODE', '') == "compliance":
         audit_path = env['CM_MLPERF_INFERENCE_AUDIT_PATH']
         shutil.copy(audit_path, env['CM_RUN_DIR'])

        if 'bert' in env['CM_MODEL']:
            env['MODEL_PATH'] = os.path.dirname(os.path.dirname(env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH']))
            env['DATASET_PATH'] = os.path.dirname(os.path.dirname(env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH']))
            env['CM_RUN_DIR'] = i['run_script_input']['path']
            env['CM_RUN_CMD'] = "bash run_bert_harness.sh " + ("--accuracy" if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy" else "")
        elif "gptj" in env['CM_MODEL']:
            if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy":
                env['LOADGEN_MODE'] = 'Accuracy'
            else:
                env['LOADGEN_MODE'] = 'Performance'
            env['INT8_MODEL_DIR'] = env['CM_ML_MODEL_PATH']
            env['CM_RUN_DIR'] = i['run_script_input']['path']
            env['CM_RUN_CMD'] = "bash run_gptj_harness.sh "

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    if env.get('CM_MLPERF_README', '') == "yes":
        import cmind as cm
        inp = i['input']
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

    if env.get('CM_DUMP_VERSION_INFO', True):
        if not state.get('mlperf-inference-implementation', {}):
            state['mlperf-inference-implementation'] = {}
        run_state = i['run_script_input']['run_state']
        state['mlperf-inference-implementation'][run_state['script_uid']] = {}
        version_info = {}
        version_info[run_state['script_uid']] = run_state['version_info']

        state['mlperf-inference-implementation']['version_info'] = version_info

    return {'return':0}
