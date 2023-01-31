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
    env['+ CXXFLAGS'] = []#"-O1 -fsanitize=address -fsanitize=undefined " ]
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
    if env.get('CM_MLPERF_DEVICE', '') == "cpu":
        env['+ CXXFLAGS'].append('-DUSE_CPU=1')
    elif env.get('CM_MLPERF_DEVICE', '') == "inferentia":
        env['+ CXXFLAGS'].append('-DUSE_INFERENTIA=1')
    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLPERF_USER_CONF' not in env:
        env['CM_MLPERF_USER_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "user.conf")

    run_suffix = ''
    run_suffix += " --mlperf_conf_path "+env['CM_MLPERF_CONF']+ ' --user_conf_path '+ env['CM_MLPERF_USER_CONF'] \
            + ' --model '+env['CM_MODEL'] \
            + ' --scenario '+env['CM_MLPERF_LOADGEN_SCENARIO'] \
            + ' --map_path ' + '/home/arjun/CM/repos/local/cache/31abfba987c242a6/preprocessed_files.txt' \
            + ' --gpu_batch_size 256 --gpu_engines /home/arjun/CM/repos/local/cache/3a3306a7be984b6b/inference_results_v2.1/closed/NVIDIA/build/engines/amd4090/resnet50/Offline/resnet50-Offline-gpu-b256-.lwis_k_99_MaxP.plan --gpu_copy_streams 1  --logfile_outdir=/tmp/a --test_mode PerformanceOnly'
    env['CM_RUN_SUFFIX'] = run_suffix

    return {'return':0}

def postprocess(i):

    env = i['env']
    if env.get('CM_MLPERF_README', 'no') == "yes":
        import cmind as cm
        inp = i['input']
        state = i['state']
        script_tags = inp['tags']
        script_adr = inp.get('add_deps_recursive', inp.get('adr', {}))

        cm_input = {'action': 'run',
                'automation': 'script',
                'tags': script_tags,
                'adr': script_adr,
                'print_deps': True,
                'quiet': True,
                'silent': True,
                'fake_run': True
                }
        r = cm.access(cm_input)
        if r['return'] > 0:
            return r

        state['mlperf-inference-implementation'] = {}
        state['mlperf-inference-implementation']['print_deps'] = r['new_state']['print_deps']

    return {'return':0}
