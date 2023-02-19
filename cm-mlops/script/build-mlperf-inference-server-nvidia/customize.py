from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if '+LIBRARY_PATH' not in env:
        env['+LIBRARY_PATH'] = []
    env['+LIBRARY_PATH'].append(os.path.join(env['CM_TENSORRT_INSTALL_PATH'], "lib"))

    cxxflags = [ "-Wno-error=switch",  "-DDALI_1_15=1", "-Wno-error=maybe-uninitialized" ]

    if env.get('CM_GCC_VERSION', '') != '':
        gcc_major_version = env['CM_GCC_VERSION'].split(".")[0]
        if int(gcc_major_version) >= 10:
            cxxflags.append("-Wno-error=range-loop-construct")

    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []

    env['+ CXXFLAGS'] += cxxflags

    return {'return':0}

def postprocess(i):

    env = i['env']
    env['MLPERF_SCRATCH_PATH'] = os.getcwd()

    return {'return':0}
