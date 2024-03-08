from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    kilt_root = env['CM_KILT_CHECKOUT_PATH']

    print(f"Harness Root: {kilt_root}")

    source_files = []
    env['CM_SOURCE_FOLDER_PATH'] = env['CM_KILT_CHECKOUT_PATH']

    env['kilt_model_root'] = env.get('CM_ML_MODEL_FILE_WITH_PATH')

    if env.get('CM_MLPERF_LOADGEN_BATCH_SIZE', '') != '':
        env['kilt_model_batch_size'] = env['CM_MLPERF_LOADGEN_BATCH_SIZE']

    if env.get('CM_QAIC_DEVICES', '') != '':
        env['kilt_device_ids'] = env['CM_QAIC_DEVICES']

    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []

    if '+CPLUS_INCLUDE_PATH' not in env:
        env['+CPLUS_INCLUDE_PATH']  = []

    if env['CM_MLPERF_DEVICE'] == "qaic":
        env['kilt_model_root'] = os.path.dirname(env['CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH'])

    if env.get('CM_MODEL') == "resnet50":
        env['dataset_imagenet_preprocessed_subset_fof'] = env['CM_DATASET_PREPROCESSED_IMAGENAMES_LIST']
        env['dataset_imagenet_preprocessed_dir'] = env['CM_DATASET_PREPROCESSED_PATH']

    elif "bert" in env.get('CM_MODEL'):
        env['dataset_squad_tokenized_max_seq_length'] = env['CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH']
        env['dataset_squad_tokenized_root'] =  env['CM_DATASET_SQUAD_TOKENIZED_ROOT']
        env['dataset_squad_tokenized_input_ids'] = os.path.basename(env['CM_DATASET_SQUAD_TOKENIZED_INPUT_IDS'])
        env['dataset_squad_tokenized_input_mask'] =  os.path.basename(env['CM_DATASET_SQUAD_TOKENIZED_INPUT_MASK'])
        env['dataset_squad_tokenized_segment_ids'] =  os.path.basename(env['CM_DATASET_SQUAD_TOKENIZED_SEGMENT_IDS'])

    elif "retinanet" in env.get('CM_MODEL'):
        env['kilt_prior_bin_path'] = os.path.join(kilt_root, "plugins", "nms-abp", "data")
        env['kilt_object_detection_preprocessed_subset_fof'] = os.path.basename(env['CM_DATASET_PREPROCESSED_IMAGENAMES_LIST'])
        env['kilt_object_detection_preprocessed_dir'] = env['CM_DATASET_PREPROCESSED_PATH']
        env['+ CXXFLAGS'].append("-DMODEL_RX50")
        env['+ CXXFLAGS'].append("-DSDK_1_11_X")

        loc_offset = env.get('CM_QAIC_MODEL_RETINANET_LOC_OFFSET')
        if loc_offset:
            env['+ CXXFLAGS'].append("-DMODEL_RX50")

        keys = [ 'LOC_OFFSET', 'LOC_SCALE', 'CONF_OFFSET', 'CONF_SCALE' ]

        if env.get('CM_RETINANET_USE_MULTIPLE_SCALES_OFFSETS', '') == 'yes':
            env['+ CXXFLAGS'].append("-DUSE_MULTIPLE_SCALES_OFFSETS=1")
            for j in range(0,4):
                keys.append(f'LOC_OFFSET{j}')
                keys.append(f'LOC_SCALE{j}')
                keys.append(f'CONF_OFFSET{j}')
                keys.append(f'CONF_SCALE{j}')

        for key in keys:
            value = env.get('CM_QAIC_MODEL_RETINANET_'+key, '')
            if value != '':
                env['+ CXXFLAGS'].append(f" -D{key}_={value} ")

    if env.get('CM_BENCHMARK', '') == 'NETWORK_BERT_SERVER':
        source_files.append(os.path.join(kilt_root, "benchmarks", "network", "bert", "server", "pack.cpp"))
        source_files.append(os.path.join(kilt_root, "benchmarks", "network", "bert", "server", "server.cpp"))
        env['+ CXXFLAGS'].append("-DNETWORK_DIVISION=1")
    elif env.get('CM_BENCHMARK', '') == 'NETWORK_BERT_CLIENT':
        #source_files.append(os.path.join(kilt_root, "benchmarks", "network", "bert", "client", "pack.cpp"))
        #env['+CPLUS_INCLUDE_PATH'].append(kilt_root) 
        #source_files.append(os.path.join(kilt_root, "benchmarks", "network", "bert", "client", "client.cpp"))
        env['+ CXXFLAGS'].append("-DNETWORK_DIVISION")
    elif env.get('CM_BENCHMARK', '') == 'STANDALONE_BERT':
        source_files.append(os.path.join(kilt_root, "benchmarks", "standalone", "bert", "pack.cpp"))

    script_path = i['run_script_input']['path']
    if env['CM_MODEL'] == "retinanet":
        env['CM_DATASET_LIST'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']


    for file in os.listdir(env['CM_SOURCE_FOLDER_PATH']):
        if file.endswith(".c") or file.endswith(".cpp"):
            source_files.append(file)

    if 'SERVER' not in env.get('CM_BENCHMARK', ''):
        source_files.append(os.path.join(kilt_root, "benchmarks", "harness", "harness.cpp"))

    #source_files.append(env['CM_QAIC_API_SRC_FILE'])

    env['+CPLUS_INCLUDE_PATH'].append(kilt_root) 
    env['+C_INCLUDE_PATH'].append(kilt_root)

    if env['CM_MLPERF_DEVICE'] == 'gpu':
        env['+C_INCLUDE_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])
        env['+CPLUS_INCLUDE_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])
        env['+LD_LIBRARY_PATH'].append(env['CM_CUDA_PATH_LIB'])
        env['+DYLD_FALLBACK_LIBRARY_PATH'].append(env['CM_CUDA_PATH_INCLUDE'])

    elif env['CM_MLPERF_DEVICE'] == 'qaic':
        source_files.append(os.path.join(kilt_root, "devices", "qaic", "api", "master", "QAicInfApi.cpp"))

    print(f"Compiling the source files: {source_files}")
    env['CM_CXX_SOURCE_FILES'] = ";".join(source_files)

    env['+ CXXFLAGS'].append("-std=c++17")
    env['+ CXXFLAGS'].append("-fpermissive")

    env['+ CXXFLAGS'].append("-DKILT_CONFIG_FROM_ENV")
    env['+ CXXFLAGS'].append("-DKILT_CONFIG_TRANSLATE_X")
    env['+ CXXFLAGS'].append("-DKILT_BENCHMARK_" + env['CM_BENCHMARK'])
    env['+ CXXFLAGS'].append("-DKILT_DEVICE_" + env['device'].upper())

    # add preprocessor flag like "#define CM_MODEL_RESNET50"
    #env['+ CXXFLAGS'].append('-DCM_MODEL_' + env['CM_MODEL'].upper())
    # add preprocessor flag like "#define CM_MLPERF_BACKEND_ONNXRUNTIME"
    env['+ CXXFLAGS'].append('-DCM_MLPERF_BACKEND_' + env['CM_MLPERF_BACKEND'].upper())
    # add preprocessor flag like "#define CM_MLPERF_DEVICE_CPU"
    env['+ CXXFLAGS'].append('-DCM_MLPERF_DEVICE_' + env['CM_MLPERF_DEVICE'].upper())

    if '+ LDCXXFLAGS' not in env:
        env['+ LDCXXFLAGS'] = [ ]

    env['+ LDCXXFLAGS'] += [
        "-lmlperf_loadgen",
        "-lpthread",
        "-ldl"
    ]
    # e.g. -lonnxruntime
    if 'CM_MLPERF_BACKEND_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_MLPERF_BACKEND_LIB_NAMESPEC'])
    # e.g. -lcudart
    if 'CM_MLPERF_DEVICE_LIB_NAMESPEC' in env:
        env['+ LDCXXFLAGS'].append('-l' + env['CM_MLPERF_DEVICE_LIB_NAMESPEC'])

    if '-DPRINT_NETWORK_DESCRIPTOR' in env['+ CXXFLAGS']:
        env['+ LDCXXFLAGS'].append('-lprotobuf')

    env['CM_LINKER_LANG'] = 'CXX'
    env['CM_RUN_DIR'] = env.get('CM_MLPERF_OUTPUT_DIR', os.getcwd())

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")
    if 'CM_MLPERF_USER_CONF' not in env:
        env['CM_MLPERF_USER_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "user.conf")

    
    env['loadgen_mlperf_conf_path'] = env['CM_MLPERF_CONF']# to LOADGEN_MLPERF_CONF
    env['loadgen_user_conf_path'] = env['CM_MLPERF_USER_CONF']# to LOADGEN_USER_CONF
    env['loadgen_scenario'] = env['CM_MLPERF_LOADGEN_SCENARIO']

    loadgen_mode = env['CM_MLPERF_LOADGEN_MODE']
    if loadgen_mode == 'performance':
        kilt_loadgen_mode = 'PerformanceOnly'
    elif loadgen_mode == 'accuracy':
        kilt_loadgen_mode = 'AccuracyOnly'
    elif loadgen_mode == 'compliance':
        kilt_loadgen_mode = 'PerformanceOnly'
    else:
        return {'return':1, 'error': 'Unknown loadgen mode'}
    env['loadgen_mode'] = kilt_loadgen_mode


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
