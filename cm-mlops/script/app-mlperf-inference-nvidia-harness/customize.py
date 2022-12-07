from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    source_files = []
    script_path = i['run_script_input']['path']

    env['CM_SOURCE_FOLDER_PATH'] = os.path.join(script_path, "src")
    endswith = [ ".c", ".cc", ".cxx", ".cpp" ]
    for file in os.listdir(env['CM_SOURCE_FOLDER_PATH']):
        if any (file.endswith(ends) for ends in endswith):
            source_files.append(file)


    if '+CPLUS_INCLUDE_PATH' not in env:
        env['+CPLUS_INCLUDE_PATH']  = []
    include_path = os.path.join(env['CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH'], 'code', 'harness', 'lwis', 'include')
    source_files.append(os.path.join(include_path, "..", "src", "lwis.cpp"))
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(script_path, include_path)) 
    env['+C_INCLUDE_PATH'].append(os.path.join(script_path, include_path))
    include_path = os.path.join(env['CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH'], 'code', 'harness', 'common')
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(script_path, include_path)) 
    env['+C_INCLUDE_PATH'].append(os.path.join(script_path, include_path))
    source_files.append(os.path.join(include_path, "logger.cpp"))

    env['CM_CXX_SOURCE_FILES'] = ";".join(source_files)

    #if '+ CXXFLAGS' not in env:
    env['+ CXXFLAGS'] = []
    env['+ CXXFLAGS'].append("-std=c++17")

    # add preprocessor flag like "#define CM_MODEL_RESNET50"
    env['+ CXXFLAGS'].append('-DCM_MODEL_' + env['CM_MODEL'].upper())
    # add preprocessor flag like "#define CM_MLPERF_DEVICE_CPU"
    env['+ CXXFLAGS'].append('-DCM_MLPERF_DEVICE_' + env['CM_MLPERF_DEVICE'].upper())

    if '+ LDCXXFLAGS' not in env:
        env['+ LDCXXFLAGS'] = [ ]

    env['+ LDCXXFLAGS'] += [
        "-lmlperf_loadgen",
        "-lpthread",
        "-lcudart",
        "-lgflags",
        "-lglog",
        "-lnuma",
        "-lnvinfer",
        "-lnvinfer_plugin",
        "-L"+env['CM_CUDA_PATH_LIB']
    ]

    env['CM_LINKER_LANG'] = 'CXX'
    env['CM_RUN_DIR'] = os.getcwd()

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLPERF_USER_CONF' not in env:
        env['CM_MLPERF_USER_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_VISION_PATH'], "user.conf")

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}
