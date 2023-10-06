from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    env = i['env']

    env['CM_MLPERF_TRAINING_NVIDIA_CODE_PATH'] = os.path.join(env['CM_MLPERF_TRAINING_RESULTS_PATH'], "NVIDIA")

    return {'return':0}
