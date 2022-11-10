from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    env = i['env']

    env['+PYTHONPATH'] = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_PATH'], "closed", "NVIDIA", "code", "common")

    return {'return':0}
