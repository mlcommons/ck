from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    clang_file_name = "clang"

    need_version = env.get('CM_VERSION','')
    cm_git_checkout = 'master' if need_version =='' else 'llvmorg-' + need_version
    print (recursion_spaces + '    # Requested git checkout: {}'.format(cm_git_checkout))
    env['CM_GIT_CHECKOUT'] = cm_git_checkout

    env['CM_LLVM_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'install', 'bin')
    env['CM_LLVM_CLANG_BIN_WITH_PATH'] = os.path.join(env['CM_LLVM_INSTALLED_PATH'], clang_file_name)
    env['CM_GET_DEPENDENT_CACHED_PATH'] = os.getcwd()

    return {'return':0}
