from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if env.get('CM_GPTJ_INTEL_MODEL', '') == 'yes':
        harness_root = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_PATH'], 'closed', 'Intel', 'code', 'gptj-99', 'pytorch-cpu')
        print(f"Harness Root: {harness_root}")
        env['CM_HARNESS_CODE_ROOT'] = harness_root
        if env['CM_ML_MODEL_WEIGHT_DATA_TYPES'] == "int8":
            env['INT8_MODEL_DIR'] = os.getcwd()
        else:
            env['INT4_MODEL_DIR'] = os.getcwd()
    else:
        path = env.get('GPTJ_CHECKPOINT_PATH', '').strip()

        if path == '' or not os.path.exists(path):
            env['CM_TMP_REQUIRE_DOWNLOAD'] = 'yes'

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['GPTJ_CHECKPOINT_PATH'] = os.path.join(env['GPTJ_CHECKPOINT_PATH'], "checkpoint-final")
    env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_CHECKPOINT_PATH']
    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}
