from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    if env.get('CM_LLVM_ENABLE_RUNTIMES', '') != '':
        enable_runtimes = env['CM_LLVM_ENABLE_RUNTIMES'].replace(":", ";")

    if env.get('CM_LLVM_ENABLE_PROJECTS', '') != '':
        enable_projects = env['CM_LLVM_ENABLE_PROJECTS'].replace(":", ";")

    llvm_build_type = env['CM_LLVM_BUILD_TYPE']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    clang_file_name = "clang"

    cmake_cmd = "cmake " + os.path.join(env["CM_LLVM_SRC_REPO_PATH"], "llvm") + " -GNinja -DCMAKE_BUILD_TYPE="+llvm_build_type + " -DLLVM_ENABLE_PROJECTS="+ enable_projects+ " -DLLVM_ENABLE_RUNTIMES='"+enable_runtimes + "' -DCMAKE_INSTALL_PREFIX=" + os.path.join(os.getcwd(), "install")+ " -DLLVM_ENABLE_RTTI=ON  -DLLVM_INSTALL_UTILS=ON "
    need_version = env.get('CM_VERSION','')
    #cm_git_checkout = 'master' if need_version =='' else 'llvmorg-' + need_version

    env['CM_LLVM_CMAKE_CMD'] = cmake_cmd

    env['CM_LLVM_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'install', 'bin')
    env['CM_LLVM_CLANG_BIN_WITH_PATH'] = os.path.join(env['CM_LLVM_INSTALLED_PATH'], clang_file_name)
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_LLVM_CLANG_BIN_WITH_PATH']

    return {'return':0}
