from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if env.get('NVIDIA_ONLY', '') == 'yes':
        env['CM_GIT_URL'] = "https://github.com/GATEOverflow/nvidia-inference-code.git"

    if 'GITHUB_REPO_OWNER' in env and '<<<GITHUB_REPO_OWNER>>>' in env['CM_GIT_URL']:
        env['CM_GIT_URL'] = env['CM_GIT_URL'].replace('<<<GITHUB_REPO_OWNER>>>', env['GITHUB_REPO_OWNER'])

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

    if env.get('CM_GIT_REPO_CURRENT_HASH', '') != '':
        env['CM_VERSION'] += "-git-"+env['CM_GIT_REPO_CURRENT_HASH']

#    env['CM_MLPERF_INFERENCE_RESULTS_PATH'] = os.path.join(os.getcwd(), "inference_results_"+env['CM_MLPERF_INFERENCE_RESULTS_VERSION_NAME'])

    return {'return':0}
