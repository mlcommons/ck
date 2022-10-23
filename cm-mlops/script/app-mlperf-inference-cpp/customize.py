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
    if 'CM_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    source_files = []
    script_path = i['run_script_input']['path']
    
    env['CM_SOURCE_FOLDER_PATH'] = os.path.join(script_path, "src")

    for file in os.listdir(env['CM_SOURCE_FOLDER_PATH']):
        if file.endswith(".c") or file.endswith(".cpp"):
            source_files.append(file)

    env['CM_CXX_SOURCE_FILES'] = ";".join(source_files)

    if '+CPLUS_INCLUDE_PATH' not in env:
        env['+CPLUS_INCLUDE_PATH']  = []

    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(script_path, "inc")) 
    env['+C_INCLUDE_PATH'].append(os.path.join(script_path, "inc"))

    # TODO: get cuda path ugly fix
    if env['CM_DEVICE'] == 'gpu':
        env['+C_INCLUDE_PATH'].append('/usr/local/cuda/include')
        env['+CPLUS_INCLUDE_PATH'].append('/usr/local/cuda/include')
        env['+LD_LIBRARY_PATH'].append('/usr/local/cuda/lib64')
        env['+DYLD_FALLBACK_LIBRARY_PATH'].append('/usr/local/cuda/lib64')

    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []
    env['+ CXXFLAGS'].append("-std=c++14")

    # add preprocessor flag like "#define CM_MODEL_RESNET50"
    env['+ CXXFLAGS'].append('-DCM_MODEL_' + env['CM_MODEL'].upper())
    # add preprocessor flag like "#define CM_BACKEND_ONNXRUNTIME"
    env['+ CXXFLAGS'].append('-DCM_BACKEND_' + env['CM_BACKEND'].upper())
    # add preprocessor flag like "#define CM_DEVICE_CPU"
    env['+ CXXFLAGS'].append('-DCM_DEVICE_' + env['CM_DEVICE'].upper())

    if '+ LDCXXFLAGS' not in env:
        env['+ LDCXXFLAGS'] = [ ]

    env['+ LDCXXFLAGS'] += [
        "-lmlperf_loadgen",
        "-lpthread"
    ]
    # e.g. -lonnxruntime
    if 'CM_BACKEND_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_BACKEND_LIB_NAMESPEC'])
    # e.g. -lcudart
    if 'CM_DEVICE_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_DEVICE_LIB_NAMESPEC'])

    env['CM_LINKER_LANG'] = 'CXX'
    env['CM_RUN_DIR'] = os.getcwd()

    if 'CM_MLC_MLPERF_CONF' not in env:
        env['CM_MLC_MLPERF_CONF'] = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLC_USER_CONF' not in env:
        env['CM_MLC_USER_CONF'] = os.path.join(env['CM_MLC_INFERENCE_VISION_PATH'], "user.conf")

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}
