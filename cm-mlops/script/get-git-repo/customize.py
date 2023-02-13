from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

#    if os_info['platform'] == 'windows':
#        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if 'CM_GIT_REPO_NAME' not in env:
        env['CM_GIT_REPO_NAME'] = os.path.basename(env['CM_GIT_URL'])

    if 'CM_GIT_DEPTH' not in env:
        env['CM_GIT_DEPTH'] = ''

    if 'CM_GIT_RECURSE_SUBMODULES' not in env:
        env['CM_GIT_RECURSE_SUBMODULES'] = ''

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']
    env['CM_GIT_CHECKOUT_PATH'] = os.path.join(os.getcwd(), env['CM_GIT_CHECKOUT_FOLDER'])

    return {'return':0}
