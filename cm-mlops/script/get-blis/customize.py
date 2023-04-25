from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    env['CM_BLIS_SRC_PATH'] = env['CM_GIT_CHECKOUT_PATH']


    return {'return':0}

def postprocess(i):

    env = i['env']
    install_dir = os.path.join(env['CM_BLIS_SRC_PATH'], "install")

    env['CM_BLIS_INSTALL_PATH'] = install_dir
    env['CM_BLIS_INC'] = os.path.join(install_dir, 'include', 'blis')
    env['CM_BLIS_LIB'] = os.path.join(install_dir, 'lib', 'libblis.a')

    blis_lib_path = os.path.join(install_dir, 'lib')

    env['+LD_LIBRARY_PATH'] = [ blis_lib_path ] if '+LD_LIBRARY_PATH' not in env else env['+LD_LIBRARY_PATH'] + [ blis_lib_path ]

    return {'return':0}


