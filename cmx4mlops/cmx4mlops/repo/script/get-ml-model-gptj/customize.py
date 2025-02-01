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


def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if env.get('CM_GPTJ_INTEL_MODEL', '') == 'yes':
        i['run_script_input']['script_name'] = 'run-intel'
        harness_root = os.path.join(
            env['CM_MLPERF_INFERENCE_RESULTS_PATH'],
            'closed',
            'Intel',
            'code',
            'gptj-99',
            'pytorch-cpu')
        print(f"Harness Root: {harness_root}")
        env['CM_HARNESS_CODE_ROOT'] = harness_root
        env['CM_CALIBRATION_CODE_ROOT'] = os.path.join(
            env['CM_MLPERF_INFERENCE_RESULTS_PATH'], 'closed', 'Intel', 'calibration')

        env['CHECKPOINT_DIR'] = env['GPTJ_CHECKPOINT_PATH']

        env['QUANTIZED_MODEL_DIR'] = os.getcwd()

        if env['CM_ML_MODEL_WEIGHT_DATA_TYPES'] == "int8":
            env['INT8_MODEL_DIR'] = os.getcwd()
        else:
            env['INT4_MODEL_DIR'] = os.getcwd()

    elif env.get('CM_TMP_ML_MODEL_PROVIDER', '') == 'nvidia':
        i['run_script_input']['script_name'] = 'run-nvidia'
        if str(env.get('CM_DOCKER_DETACHED_MODE', '')
               ).lower() in ['yes', 'true', "1"]:
            env['DOCKER_RUN_OPTS'] = "--rm --ipc=host --ulimit memlock=-1 --ulimit stack=67108864"
        gpu_arch = int(
            float(
                env['CM_CUDA_DEVICE_PROP_GPU_COMPUTE_CAPABILITY']) *
            10)
        env['CM_GPU_ARCH'] = gpu_arch
        env['CM_TMP_REQUIRE_DOWNLOAD'] = 'no'

    else:
        is_saxml = env.get('CM_TMP_MODEL_SAXML', '')
        if is_saxml == "fp32":
            i['run_script_input']['script_name'] = 'run-saxml'
        elif is_saxml == "int8":
            i['run_script_input']['script_name'] = 'run-saxml-quantized'
        else:
            path = env.get('GPTJ_CHECKPOINT_PATH', '').strip()

            if path == '' or not os.path.exists(path):
                env['CM_TMP_REQUIRE_DOWNLOAD'] = 'yes'

    return {'return': 0}


def postprocess(i):

    env = i['env']

    if os.path.exists(os.path.join(
            env['GPTJ_CHECKPOINT_PATH'], "checkpoint-final")):
        env['GPTJ_CHECKPOINT_PATH'] = os.path.join(
            env['GPTJ_CHECKPOINT_PATH'], "checkpoint-final")

    is_saxml = env.get('CM_TMP_MODEL_SAXML', '')
    if is_saxml == "fp32":
        if os.path.exists("pax_gptj_checkpoint"):
            env['GPTJ_SAXML_CHECKPOINT_PATH'] = os.path.join(
                os.getcwd(), "pax_gptj_checkpoint")
            env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_SAXML_CHECKPOINT_PATH']
        else:
            return {'return': 1, 'error': 'pax_gptj_checkpoint generation failed'}

    elif is_saxml == "int8":
        if os.path.exists("int8_ckpt"):
            env['GPTJ_SAXML_INT8_CHECKPOINT_PATH'] = os.path.join(
                os.getcwd(), "int8_ckpt")
            env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_SAXML_INT8_CHECKPOINT_PATH']
        else:
            return {'return': 1, 'error': 'pax_gptj_checkpoint generation failed'}
    elif env.get('CM_TMP_ML_MODEL_PROVIDER', '') == 'nvidia':
        env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(
            env['CM_NVIDIA_MLPERF_SCRATCH_PATH'],
            'models',
            'GPTJ-6B',
            'fp8-quantized-ammo',
            'GPTJ-FP8-quantized')
    else:
        env['CM_ML_MODEL_FILE_WITH_PATH'] = env['GPTJ_CHECKPOINT_PATH']

    env['CM_ML_MODEL_FILE'] = os.path.basename(
        env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return': 0}
