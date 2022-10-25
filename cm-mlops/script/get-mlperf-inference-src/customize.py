from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    if 'CM_GIT_DEPTH' not in env:
        env['CM_GIT_DEPTH'] = ''
    
    if 'CM_GIT_RECURSE_SUBMODULES' not in env:
        env['CM_GIT_RECURSE_SUBMODULES'] = ''

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    env['CM_MLPERF_INFERENCE_SOURCE'] = os.path.join(os.getcwd(), 'inference')
    env['CM_MLPERF_INFERENCE_VISION_PATH'] = os.path.join(os.getcwd(), 'inference', 'vision', 'classification_and_detection')
    env['CM_MLPERF_INFERENCE_BERT_PATH'] = os.path.join(os.getcwd(), 'inference', 'language', 'bert')
    env['CM_MLPERF_INFERENCE_RNNT_PATH'] = os.path.join(os.getcwd(), 'inference', 'speech_recognition', 'rnnt')
    env['CM_MLPERF_INFERENCE_DLRM_PATH'] = os.path.join(os.getcwd(), 'inference', 'recommendation', 'dlrm')

#        20221024: we save and restore env in the main script and can clean env here for determinism
#    if '+PYTHONPATH' not in env: env['+PYTHONPATH'] = []
    env['+PYTHONPATH']=[]
    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_INFERENCE_VISION_PATH'], 'python'))
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
