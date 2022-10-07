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

    if 'CM_GIT_CHECKOUT' not in env:
        env['CM_GIT_CHECKOUT'] = 'releases/gcc-' + need_version
    bazel_bin = "bazel"
    env['CM_BAZEL_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'install', 'bin')
    env['CM_BAZEL_BIN_WITH_PATH'] = os.path.join(os.getcwd(), 'install', 'bin', bazel_bin)
    env['CM_TMP_GET_DEPENDENT_CACHED_PATH'] =  os.getcwd()

    return {'return':0}
