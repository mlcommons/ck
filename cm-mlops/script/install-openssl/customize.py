from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_VERSION','')
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    return {'return':0}

def postprocess(i):
    inp = i['input']
    env = i['env']
    tags = inp['tags']
    tag_list = tags.split(",")
    install_path = os.path.join(os.getcwd(), 'openssl-'+env['CM_VERSION']+'g', 'install')
    path_lib = os.path.join(install_path, 'lib')
    if '+LD_LIBRARY_PATH' not in env:
        env['+LD_LIBRARY_PATH'] = []
    env['+LD_LIBRARY_PATH'].append(path_lib)
    bin_name = "openssl"
    path_bin = os.path.join(install_path, 'bin')
    env['CM_OPENSSL_INSTALLED_PATH'] = path_bin
    env['CM_OPENSSL_BIN_WITH_PATH'] = os.path.join(path_bin, bin_name)
    return {'return':0}
