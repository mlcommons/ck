from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    if 'CM_MLPERF_PTD_PATH' not in env:
        env['CM_MLPERF_PTD_PATH'] = os.path.join(env['CM_MLPERF_POWER_SOURCE'], 'inference_v1.0', 'ptd-linux-x86')
    env['CM_SPEC_PTD_PATH'] = env['CM_MLPERF_PTD_PATH']

    return {'return':0}
