from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if 'CM_GIT_CHECKOUT_PATH' not in env:
        return {'return':1, 'error': 'CM_GIT_CHECKOUT_PATH is not set'}

    env['CM_GIT_PULL_CMD'] = "git pull --rebase"

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
