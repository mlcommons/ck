from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    if env.get('CM_INPUT') and not env.get('CM_MLPERF_PTD_PATH'):
        env['CM_MLPERF_PTD_PATH'] = env['CM_INPUT']

    if 'CM_GIT_DEPTH' not in env:
        env['CM_GIT_DEPTH'] = ''

    if 'CM_GIT_RECURSE_SUBMODULES' not in env:
        env['CM_GIT_RECURSE_SUBMODULES'] = ''

    need_version = env.get('CM_VERSION','')
    versions = meta['versions']

    if need_version!='' and not need_version in versions:
        env['CM_GIT_CHECKOUT'] = need_version

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    if 'CM_MLPERF_PTD_PATH' not in env:
        env['CM_MLPERF_PTD_PATH'] = os.path.join(os.getcwd(), 'power', 'inference_v1.0', 'ptd-linux-x86')
    env['CM_SPEC_PTD_PATH'] = env['CM_MLPERF_PTD_PATH']

    return {'return':0}
