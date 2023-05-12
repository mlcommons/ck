from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    env['CM_QAIC_COMPUTE_SDK_PATH'] = env['CM_GIT_CHECKOUT_PATH']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']
    #env['CM_QAIC_RUNNER_PATH'] = os.path.join(env['CM_QAIC_SOFTWARE_KIT_PATH'], "build", "utils", "qaic-runner")

    if '+PATH' not in env:
      env['+PATH'] = []

    env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH'] = os.path.join(env['CM_QAIC_COMPUTE_SDK_PATH'], "install", "qaic-compute-"+env['CM_QAIC_COMPUTE_SDK_INSTALL_MODE'])

    env['QAIC_COMPUTE_INSTALL_DIR'] = env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH']

    env['+PATH'].append(os.path.join(env['CM_QAIC_COMPUTE_SDK_INSTALL_PATH'], "exec"))

    return {'return':1}
