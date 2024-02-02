from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_NVIDIA_MLPERF_SCRATCH_PATH', '') == '':
        if env.get('MLPERF_SCRATCH_PATH','') != '':
            env['CM_NVIDIA_MLPERF_SCRATCH_PATH'] = env['MLPERF_SCRATCH_PATH']
        else:
            env['CM_NVIDIA_MLPERF_SCRATCH_PATH'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['MLPERF_SCRATCH_PATH'] = env['CM_NVIDIA_MLPERF_SCRATCH_PATH']
    env['CM_GET_DEPENDENT_CACHED_PATH'] =  env['CM_NVIDIA_MLPERF_SCRATCH_PATH']

    return {'return':0}
