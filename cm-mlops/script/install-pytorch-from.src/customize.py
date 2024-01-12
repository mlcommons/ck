from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    env['+ CXXFLAGS'] = [ "-Wno-error", "-unqualified-std-cast-call" ]
    env['CMAKE_CXX_FLAGS'] = "-Wno-error -unqualified-std-cast-call"
    run_cmd="CC="+os.path.join(env['CM_LLVM_INSTALLED_PATH'], 'clang') + " CXX="+ os.path.join(env['CM_LLVM_INSTALLED_PATH'], 'clang++') +" USE_CUDA=OFF python3 -m pip install -e ."

    env['CM_RUN_CMD'] = run_cmd

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    return {'return':0}
