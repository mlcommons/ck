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
    master_model = ml_model.replace("-99", "").replace("-99.9","")
    master_model = master_model.replace("gptj", "gpt-j")

    backend = env['CM_MLPERF_BACKEND']
    device = env['CM_MLPERF_DEVICE']
    harness_root = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_PATH'], 'closed', 'Intel', 'code', ml_model, backend+"-"+device)

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

    if env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "calibration":
        calibration_root = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_PATH'], 'closed', 'Intel', 'calibration', master_model, backend+"-"+device)

        if "gpt" in env['CM_MODEL']:
            i['run_script_input']['script_name'] = "calibrate_gptj_int4_model"
            calibration_path = os.path.join(calibration_root, "INT4")
            env['CM_MLPERF_INFERENCE_INTEL_CALIBRATION_PATH'] = calibration_path
            env['INT4_CALIBRATION_DIR'] = os.path.join(calibration_path, "data", "quantized-int4-model")


    elif env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "build_harness":
        print(f"Harness Root: {harness_root}")
        if "bert" in env['CM_MODEL']:
            i['run_script_input']['script_name'] = "build_bert_harness"
            env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH'] = os.path.join(os.getcwd(), "harness", "build", "bert_inference")
            env['DATA_PATH'] = os.path.join(os.getcwd(), "harness", "bert")
        elif "gpt" in env['CM_MODEL']:
            i['run_script_input']['script_name'] = "build_gptj_harness"
            env['CM_MLPERF_INFERENCE_INTEL_HARNESS_PATH'] = os.path.join(os.getcwd(), "harness", "build", "gptj_inference")
            env['DATA_PATH'] = os.path.join(os.getcwd(), "harness", "gptj")
            env['MLPERF_INFERENCE_ROOT'] = env['CM_MLPERF_INFERENCE_SOURCE']
            if env.get('INTEL_GPTJ_INT4', '') == 'yes':
                model_precision = "int4"
                env['RUN_QUANTIZATION_CMD'] = "bash run_quantization_int4.sh"
            else:
                model_precision = "int8"
                env['RUN_QUANTIZATION_CMD'] = "bash run_quantization.sh"
            final_model_path = os.path.join(harness_root, "data", f"gpt-j-{model_precision}-model", "best_model.pt")
            model_dir_name = f"{model_precision.upper()}_MODEL_DIR"
            env[model_dir_name] = os.path.dirname(final_model_path)
            if not os.path.exists(env[model_dir_name]):
                os.makedirs(env[model_dir_name])
            env['CM_ML_MODEL_PATH'] = env[model_dir_name]
            if env.get('CM_MLPERF_INFERENCE_INTEL_GPTJ_INT8_MODEL_PATH', '') != '' and env.get('INT8_MODEL_DIR', '') != '':
                shutil.copy(env['CM_MLPERF_INFERENCE_INTEL_GPTJ_INT8_MODEL_PATH'], env[model_dir_name])
            if env.get('CM_MLPERF_INFERENCE_INTEL_GPTJ_INT4_MODEL_PATH', '') != '' and env.get('INT4_MODEL_DIR', '') != '':
                shutil.copy(env['CM_MLPERF_INFERENCE_INTEL_GPTJ_INT4_MODEL_PATH'], env[model_dir_name])

    elif env['CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE'] == "run_harness":
        print(f"Harness Root: {harness_root}")
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
            if env.get('INTEL_GPTJ_INT4', '') == 'yes':
                model_precision = "int4"
                env['INT4_MODEL_DIR'] = env['CM_ML_MODEL_PATH']
                env['QUANTIZED_MODEL'] = os.path.join(env['INT4_MODEL_DIR'], "best_int4_model.pt")
                env['PRECISION'] = "int4_bf16_mixed"
            else:
                env['INT8_MODEL_DIR'] = env['CM_ML_MODEL_PATH']
                env['QUANTIZED_MODEL'] = os.path.join(env["INT8_MODEL_DIR"], "best_model.pt")
                env['PRECISION'] = "int8"
            env['CM_RUN_DIR'] = i['run_script_input']['path']
            env['CM_RUN_CMD'] = "bash run_gptj_harness.sh "

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
