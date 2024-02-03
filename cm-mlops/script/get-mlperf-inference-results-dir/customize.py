from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_MLPERF_INFERENCE_RESULTS_DIR','') == '':
        env['CM_MLPERF_INFERENCE_RESULTS_DIR'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  env['CM_MLPERF_INFERENCE_RESULTS_DIR']

    return {'return':0}
