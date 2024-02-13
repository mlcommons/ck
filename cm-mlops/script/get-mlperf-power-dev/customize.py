from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    return {'return':0}


def postprocess(i):

    env = i['env']
    if env.get('CM_VERSION', '') == '':
        env['CM_VERSION'] = "master"

    if env.get('CM_GIT_REPO_CURRENT_HASH', '') != '':
        env['CM_VERSION'] += "-git-"+env['CM_GIT_REPO_CURRENT_HASH']

    return {'return':0}
