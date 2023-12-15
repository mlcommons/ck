from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    if env.get('CM_ML_MODEL_BERT_PACKED', '') == 'yes':
        i['run_script_input']['script_name'] = "run-packed"
        env['CM_BERT_CONFIG_PATH'] = os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'], "bert_config.json")
        env['CM_BERT_CHECKPOINT_DOWNLOAD_DIR'] = os.getcwd()
        env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(os.getcwd(), "model.onnx")
        env['CM_ML_MODEL_BERT_PACKED_PATH'] = os.path.join(os.getcwd(), "model.onnx")

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])

    if env.get('CM_ML_MODEL_PRECISION', '') == "fp32":
        env['CM_ML_MODEL_BERT_LARGE_FP32_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']
    elif env.get('CM_ML_MODEL_PRECISION', '') == "int8":
        env['CM_ML_MODEL_BERT_LARGE_INT8_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}

