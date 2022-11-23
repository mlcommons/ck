from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    if '+PYTHONPATH' not in env:
        env['+PYTHONPATH'] = []
    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_TRAINING_SOURCE'], "single_stage_detector", "ssd"))

    print(env)


    return {'return':0}
