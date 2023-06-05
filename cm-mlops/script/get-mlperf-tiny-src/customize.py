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

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    env['CM_MLPERF_TINY_SRC'] = os.path.join(os.getcwd(), 'src')
    env['CM_MLPERF_TINY_BENCHMARK'] = os.path.join(os.getcwd(), 'src', 'benchmark')
    env['CM_MLPERF_TINY_DATASETS'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets')
    env['CM_MLPERF_TINY_DATASETS_AD'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets', 'ad01')
    env['CM_MLPERF_TINY_DATASETS_IC'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets', 'ic01')
    env['CM_MLPERF_TINY_DATASETS_KWS'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets', 'kws01')
    env['CM_MLPERF_TINY_DATASETS_KWS_OPEN'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets', 'kws01-open')
    env['CM_MLPERF_TINY_DATASETS_VWW'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'evaluation', 'datasets', 'vww01')
    env['CM_MLPERF_TINY_TRAINING'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'training')
    env['CM_MLPERF_TINY_TRAINING_AD'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'training', 'anomaly_detection')
    env['CM_MLPERF_TINY_TRAINING_IC'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'training', 'image_classification')
    env['CM_MLPERF_TINY_TRAINING_KWS'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'training', 'keyword_spotting')
    env['CM_MLPERF_TINY_TRAINING_VWW'] = os.path.join(os.getcwd(), 'src', 'benchmark', 'training', 'visual_wake_words')

#        20221024: we save and restore env in the main script and can clean env here for determinism
#    if '+PYTHONPATH' not in env: env['+PYTHONPATH'] = []
#    env['+PYTHONPATH']=[]
#    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], 'python'))
#    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], 'tools', 'submission'))

    return {'return':0}
