from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    automation = i['automation']

    meta = i['meta']

    if os_info['platform'] == 'windows':
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('WARNING: this script was not thoroughly tested on Windows and compilation may fail - please help us test and improve it!')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#        # Currently support only LLVM on Windows
#        print ('# Forcing LLVM on Windows')        
#        r = automation.update_deps({'deps':meta['post_deps'], 'update_deps':{'compile-program': {'adr':{'compiler':{'tags':'llvm'}}}}})
#        if r['return']>0: return r
    
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    source_files = []
    script_path = i['run_script_input']['path']
    if env['CM_MODEL'] == "retinanet":
        env['CM_DATASET_LIST'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']
    env['CM_SOURCE_FOLDER_PATH'] = os.path.join(script_path, "src")

    for file in os.listdir(env['CM_SOURCE_FOLDER_PATH']):
        if file.endswith(".c") or file.endswith(".cpp"):
            source_files.append(file)

    env['CM_CXX_SOURCE_FILES'] = ";".join(source_files)

    if '+CPLUS_INCLUDE_PATH' not in env:
        env['+CPLUS_INCLUDE_PATH']  = []

    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(script_path, "inc")) 
    env['+C_INCLUDE_PATH'].append(os.path.join(script_path, "inc"))

    if env['CM_MLPERF_DEVICE'] == 'gpu':
        env['+C_INCLUDE_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])
        env['+CPLUS_INCLUDE_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])
        env['+LD_LIBRARY_PATH'].append(env['CM_CUDA_PATH_LIB'])
        env['+DYLD_FALLBACK_LIBRARY_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])

    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []
    env['+ CXXFLAGS'].append("-std=c++14")

    # add preprocessor flag like "#define CM_MODEL_RESNET50"
    env['+ CXXFLAGS'].append('-DCM_MODEL_' + env['CM_MODEL'].upper())
    # add preprocessor flag like "#define CM_MLPERF_BACKEND_ONNXRUNTIME"
    env['+ CXXFLAGS'].append('-DCM_MLPERF_BACKEND_' + env['CM_MLPERF_BACKEND'].upper())
    # add preprocessor flag like "#define CM_MLPERF_DEVICE_CPU"
    env['+ CXXFLAGS'].append('-DCM_MLPERF_DEVICE_' + env['CM_MLPERF_DEVICE'].upper())

    if '+ LDCXXFLAGS' not in env:
        env['+ LDCXXFLAGS'] = [ ]

    env['+ LDCXXFLAGS'] += [
        "-lmlperf_loadgen",
        "-lpthread"
    ]
    # e.g. -lonnxruntime
    if 'CM_MLPERF_BACKEND_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_MLPERF_BACKEND_LIB_NAMESPEC'])
    # e.g. -lcudart
    if 'CM_MLPERF_DEVICE_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_MLPERF_DEVICE_LIB_NAMESPEC'])

    env['CM_LINKER_LANG'] = 'CXX'
    env['CM_RUN_DIR'] = os.getcwd()

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLPERF_USER_CONF' not in env:
        env['CM_MLPERF_USER_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "user.conf")

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
