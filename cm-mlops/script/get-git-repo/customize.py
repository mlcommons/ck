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

    if env.get('CM_GIT_CHECKOUT', '') == '':
        env['CM_GIT_CHECKOUT'] = env.get('CM_GIT_SHA', env.get('CM_GIT_BRANCH', ''))

    git_checkout_string = " -b "+ env['CM_GIT_BRANCH'] if ("CM_GIT_BRANCH" in env and env.get('CM_GIT_SHA', '') == '') else ""

    git_clone_cmd = "git clone " + env['CM_GIT_RECURSE_SUBMODULES'] +  git_checkout_string + " " + env['CM_GIT_URL'] + " " + env.get('CM_GIT_DEPTH','') + ' ' + env['CM_GIT_CHECKOUT_FOLDER']

    env['CM_GIT_CLONE_CMD'] = git_clone_cmd
    env['CM_TMP_GIT_PATH'] = os.path.join(os.getcwd(), env['CM_GIT_CHECKOUT_FOLDER'], ".git")

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']
    env['CM_GIT_CHECKOUT_PATH'] = os.path.join(os.getcwd(), env['CM_GIT_CHECKOUT_FOLDER'])
    git_checkout_path = env['CM_GIT_CHECKOUT_PATH']

    # We remap CM_GIT variables with CM_GIT_REPO prefix so that they don't contaminate the env of the parent script
    env['CM_GIT_REPO_CHECKOUT_PATH'] = env['CM_GIT_CHECKOUT_PATH']
    env['CM_GIT_REPO_URL'] = env['CM_GIT_URL']
    env['CM_GIT_REPO_CHECKOUT'] = env['CM_GIT_CHECKOUT']
    env['CM_GIT_REPO_DEPTH'] = env['CM_GIT_DEPTH']
    env['CM_GIT_REPO_CHECKOUT_FOLDER'] = env['CM_GIT_CHECKOUT_FOLDER']
    env['CM_GIT_REPO_PATCH'] = env['CM_GIT_PATCH']
    env['CM_GIT_REPO_RECURSE_SUBMODULES'] = env['CM_GIT_RECURSE_SUBMODULES']

    if env.get('CM_GIT_CHECKOUT_PATH_ENV_NAME','') != '' and env.get(env['CM_GIT_CHECKOUT_PATH_ENV_NAME'], '') == '':
        env[env['CM_GIT_CHECKOUT_PATH_ENV_NAME']] = git_checkout_path

    env['CM_GET_DEPENDENT_CACHED_PATH'] = git_checkout_path

    return {'return':0}
