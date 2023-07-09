from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

#    if os_info['platform'] == 'windows':
#        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if 'CM_GIT_DEPTH' not in env:
        env['CM_GIT_DEPTH'] = ''

    if 'CM_GIT_RECURSE_SUBMODULES' not in env:
        env['CM_GIT_RECURSE_SUBMODULES'] = ''
    submodules = []
    possible_submodules = {
            "gn": "third_party/gn",
            "pybind": "third_party/pybind",
            "deeplearningexamples":"language/bert/DeepLearningExamples",
            "3d-unet":"vision/medical_imaging/3d-unet-brats19/nnUnet"
            }
    for submodule in possible_submodules:
        env_name = submodule.upper().replace("-","_")
        if env.get("CM_SUBMODULE_"+env_name) == "yes":
            submodules.append(possible_submodules[submodule])

    env['CM_GIT_SUBMODULES'] = ",".join(submodules)
    need_version = env.get('CM_VERSION','')
    versions = meta['versions']

    if need_version!='' and not need_version in versions:
        env['CM_GIT_CHECKOUT'] = need_version

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    #env['CM_MLPERF_INFERENCE_SOURCE'] = os.path.join(os.getcwd(), 'inference')
    env['CM_MLPERF_INFERENCE_VISION_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision')
    env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision', 'classification_and_detection')
    env['CM_MLPERF_INFERENCE_BERT_PATH'] = os.path.join(os.getcwd(), 'inference', 'language', 'bert')
    env['CM_MLPERF_INFERENCE_RNNT_PATH'] = os.path.join(os.getcwd(), 'inference', 'speech_recognition', 'rnnt')
    env['CM_MLPERF_INFERENCE_DLRM_PATH'] = os.path.join(os.getcwd(), 'inference', 'recommendation', 'dlrm')
    env['CM_MLPERF_INFERENCE_3DUNET_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision', 'medical_imaging', '3d-unet-kits19')
    env['CM_MLPERF_INFERENCE_CONF_PATH'] = os.path.join(os.getcwd(), 'inference', 'mlperf.conf')

#        20221024: we save and restore env in the main script and can clean env here for determinism
#    if '+PYTHONPATH' not in env: env['+PYTHONPATH'] = []
    env['+PYTHONPATH']=[]
    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], 'python'))
    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], 'tools', 'submission'))

    valid_models = get_valid_models(env['CM_MLPERF_LAST_RELEASE'], env['CM_MLPERF_INFERENCE_SOURCE'])

    state['CM_MLPERF_INFERENCE_MODELS'] = valid_models

    return {'return':0}


def get_valid_models(mlperf_version, mlperf_path):

    import sys

    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")

    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))

    import submission_checker as checker

    config = checker.MODEL_CONFIG

    valid_models = config[mlperf_version]["models"]

    return valid_models
