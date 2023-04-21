from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    env['ZENDNN_BLIS_PATH'] = env['CM_BLIS_INSTALL_PATH']
    env['ZENDNN_LIBM_PATH'] = env['CM_AOCL_BUILD_PATH']

    env['ZENDNN_SRC_PATH'] = env['CM_GIT_REPO_CHECKOUT_PATH']

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
