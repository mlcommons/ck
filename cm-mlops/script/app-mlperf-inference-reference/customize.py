from cmind import utils
import os
import json
import shutil
import subprocess

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    if env.get('CM_MLPERF_POWER','') == "yes":
        power = "yes"
    else:
        power = "no"

    rerun = True if env.get("CM_RERUN","")!='' else False

    if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
        env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if 'CM_MLPERF_LOADGEN_MODE' not in env:
        env['CM_MLPERF_LOADGEN_MODE'] = "accuracy"

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': "Please select a variation specifying the model to run"}

    if env['CM_MODEL'] == "resnet50":
        cmd = "cp " + os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt") + " " + os.path.join(env['CM_DATASET_PATH'],
        "val_map.txt")
        ret = os.system(cmd)

    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] = ""

    if 'CM_MLPERF_LOADGEN_QPS' not in env:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = " --qps " + env['CM_MLPERF_LOADGEN_QPS']

    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_MLPERF_LOADGEN_QPS_OPT']

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_HOST_CPU_TOTAL_CORES']) // \
                    (int(env.get('CM_HOST_CPU_SOCKETS', '1')) * int(env.get('CM_HOST_CPU_TOTAL_CORES', '1'))))
        else:
            env['CM_NUM_THREADS'] = env.get('CM_HOST_CPU_TOTAL_CORES', '1')

    if env.get('CM_MLPERF_LOADGEN_MAX_BATCHSIZE','') != '' and not env.get('CM_MLPERF_MODEL_SKIP_BATCHING', False) :
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --max-batchsize " + env['CM_MLPERF_LOADGEN_MAX_BATCHSIZE']

    if env.get('CM_MLPERF_LOADGEN_QUERY_COUNT','') != '' and not env.get('CM_TMP_IGNORE_MLPERF_QUERY_COUNT', False) and env['CM_MLPERF_LOADGEN_MODE'] == 'accuracy' and env.get('CM_MLPERF_RUN_STYLE','') != "valid":
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --count " + env['CM_MLPERF_LOADGEN_QUERY_COUNT']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")


    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] +=  " --mlperf_conf '" + env['CM_MLPERF_CONF'] + "'"

    env['MODEL_DIR'] = env.get('CM_ML_MODEL_PATH', os.path.dirname(env.get('CM_ML_MODEL_FILE_WITH_PATH')))

    RUN_CMD = ""
    state['RUN'] = {}
    test_list = ["TEST01", "TEST04", "TEST05"]
    if env['CM_MODEL'] in ["rnnt", "bert-99", "bert-99.9", "dlrm-99", "dlrm-99.9", "3d-unet-99", "3d-unet-99.9"]:
        test_list.remove("TEST04")

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    state['RUN'][scenario] = {}
    scenario_extra_options = ''

    NUM_THREADS = env['CM_NUM_THREADS']

    if env['CM_MODEL'] in  [ 'resnet50', 'retinanet'] :
        scenario_extra_options +=  " --threads " + NUM_THREADS

    ml_model_name = env['CM_MODEL']
    if 'CM_MLPERF_USER_CONF' in env:
        user_conf_path = env['CM_MLPERF_USER_CONF']
        scenario_extra_options +=  " --user_conf '" + user_conf_path + "'"

    mode = env['CM_MLPERF_LOADGEN_MODE']
    mode_extra_options = ""

    if 'CM_DATASET_PREPROCESSED_PATH' in env and env['CM_MODEL'] in  [ 'resnet50', 'retinanet' ]:
        #dataset_options = " --use_preprocessed_dataset --preprocessed_dir "+env['CM_DATASET_PREPROCESSED_PATH']
        dataset_options = " --use_preprocessed_dataset --cache_dir "+env['CM_DATASET_PREPROCESSED_PATH']
        if env['CM_MODEL'] == "retinanet":
            dataset_options += " --dataset-list "+ env['CM_DATASET_ANNOTATIONS_FILE_PATH']
        elif env['CM_MODEL'] == "resnet50":
            dataset_options += " --dataset-list "+ os.path.join(env['CM_DATASET_PATH'], "val_map.txt")
        env['DATA_DIR'] = env.get('CM_DATASET_PREPROCESSED_PATH')
    else:
        if 'CM_DATASET_PREPROCESSED_PATH' in env:
            env['DATA_DIR'] = env.get('CM_DATASET_PREPROCESSED_PATH')
        else:
            env['DATA_DIR'] = env.get('CM_DATASET_PATH')
        dataset_options = ''

    if env.get('CM_MLPERF_EXTRA_DATASET_ARGS','') != '':
        dataset_options += " " + env['CM_MLPERF_EXTRA_DATASET_ARGS']

    if mode == "accuracy":
        mode_extra_options += " --accuracy"

    elif mode == "performance":
        pass

    elif mode == "compliance":

        audit_full_path = env['CM_MLPERF_INFERENCE_AUDIT_PATH']
        mode_extra_options = " --audit '" + audit_full_path + "'"

    if env.get('CM_MLPERF_OUTPUT_DIR', '') == '':
        env['CM_MLPERF_OUTPUT_DIR'] = os.getcwd()

    mlperf_implementation = env.get('CM_MLPERF_IMPLEMENTATION', 'reference') 
    cmd = get_run_cmd(env, scenario_extra_options, mode_extra_options, dataset_options, mlperf_implementation)

    env['CM_MLPERF_RUN_CMD'] = cmd
    env['CM_RUN_DIR'] = os.getcwd()
    env['CM_RUN_CMD'] = cmd
    env['CK_PROGRAM_TMP_DIR'] = env.get('CM_ML_MODEL_PATH') #for tvm

    if env.get('CM_HOST_PLATFORM_FLAVOR','') == "arm64":
        env['CM_HOST_PLATFORM_FLAVOR'] = "aarch64"

    return {'return':0}

def get_run_cmd(env, scenario_extra_options, mode_extra_options, dataset_options, implementation="reference"):
    if implementation == "reference":
        return get_run_cmd_reference(env, scenario_extra_options, mode_extra_options, dataset_options)
    if implementation == "nvidia":
        return get_run_cmd_nvidia(env, scenario_extra_options, mode_extra_options, dataset_options)
    return ""


def get_run_cmd_reference(env, scenario_extra_options, mode_extra_options, dataset_options):

    if env['CM_MODEL'] in [ "gptj" ]:

        env['RUN_DIR'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "language", "gpt-j")
        cmd =  "cd '"+ env['RUN_DIR'] + "' &&  "+ env['CM_PYTHON_BIN_WITH_PATH'] +  \
            " main.py --model-path=" + env['CM_ML_MODEL_FILE_WITH_PATH'] + ' --dataset-path=' + env['CM_DATASET_EVAL_PATH'] + " --scenario " + env['CM_MLPERF_LOADGEN_SCENARIO'] + " " + env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + \
            ' --dtype ' + env['CM_MLPERF_MODEL_PRECISION'] + \
            scenario_extra_options + mode_extra_options + dataset_options
        cmd = cmd.replace("--count", "--max_examples")
        if env['CM_MLPERF_DEVICE'] == "gpu":
            gpu_options = " --gpu"
            env['CUDA_VISIBLE_DEVICES'] = "0"
        else:
            gpu_options = ""
        cmd = cmd + gpu_options
        env['LOG_PATH'] = env['CM_MLPERF_OUTPUT_DIR']
        return cmd

    if env['CM_MODEL'] in [ "resnet50", "retinanet" ]:

        env['RUN_DIR'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "vision", "classification_and_detection")
        if env.get('CM_MLPERF_VISION_DATASET_OPTION','') == '':
            cmd =  "cd '"+ env['RUN_DIR'] + "' && OUTPUT_DIR='" + env['CM_MLPERF_OUTPUT_DIR'] + "' ./run_local.sh " + env['CM_MLPERF_BACKEND'] + ' ' + \
            env['CM_MODEL'] + ' ' + env['CM_MLPERF_DEVICE'] + " --scenario " + env['CM_MLPERF_LOADGEN_SCENARIO'] + " " + env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + \
            scenario_extra_options + mode_extra_options + dataset_options
            return cmd

        env['MODEL_FILE'] = env.get('CM_MLPERF_CUSTOM_MODEL_PATH', env.get('CM_ML_MODEL_FILE_WITH_PATH'))
        if not env['MODEL_FILE']:
            return {'return': 1, 'error': 'No valid model file found!'}

        env['LOG_PATH'] = env['CM_MLPERF_OUTPUT_DIR']
        
        extra_options = " --output "+ env['CM_MLPERF_OUTPUT_DIR'] +" --model-name resnet50  --dataset " + env['CM_MLPERF_VISION_DATASET_OPTION'] + ' --max-batchsize ' + env.get('CM_MLPERF_LOADGEN_MAX_BATCHSIZE', '1') + \
                " --dataset-path "+env['CM_DATASET_PREPROCESSED_PATH']+" --model "+env['MODEL_FILE'] + \
                " --preprocessed_dir "+env['CM_DATASET_PREPROCESSED_PATH']

        cmd = "cd '" + os.path.join(env['RUN_DIR'],"python") + "' && "+env['CM_PYTHON_BIN_WITH_PATH']+ " main.py "+\
        "--backend "+env['CM_MLPERF_BACKEND']+ " --scenario="+env['CM_MLPERF_LOADGEN_SCENARIO'] + \
            env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options + dataset_options + extra_options
        env['SKIP_VERIFY_ACCURACY'] = True

    elif "bert" in env['CM_MODEL']:

        env['RUN_DIR'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "language", "bert")
        env['MODEL_FILE'] = env.get('CM_MLPERF_CUSTOM_MODEL_PATH', env.get('CM_ML_MODEL_FILE_WITH_PATH'))
        if not env['MODEL_FILE']:
            return {'return': 1, 'error': 'No valid model file found!'}
        if env.get('CM_MLPERF_QUANTIZATION') in [ "on", True, "1", "True" ]:
            quantization_options = " --quantized"
        else:
            quantization_options = ""
        cmd = "cd '" + env['RUN_DIR'] + "' && "+env['CM_PYTHON_BIN_WITH_PATH']+ " run.py --backend=" + env['CM_MLPERF_BACKEND'] + " --scenario="+env['CM_MLPERF_LOADGEN_SCENARIO'] + \
            env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options + dataset_options + quantization_options
        if env['CM_MLPERF_BACKEND'] == "deepsparse":
            cmd += " --batch_size=" + env.get('CM_MLPERF_LOADGEN_MAX_BATCHSIZE', '1') + " --model_path=" + env['MODEL_FILE']

        if env.get('CM_MLPERF_CUSTOM_MODEL_PATH', '') != '':
            env['CM_ML_MODEL_FILE_WITH_PATH'] = env['MODEL_FILE']

        cmd = cmd.replace("--count", "--max_examples")
        env['VOCAB_FILE'] = env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH']
        env['DATASET_FILE'] = env['CM_DATASET_SQUAD_VAL_PATH']
        env['LOG_PATH'] = env['CM_MLPERF_OUTPUT_DIR']
        env['SKIP_VERIFY_ACCURACY'] = True

    elif "rnnt" in env['CM_MODEL']:

        env['RUN_DIR'] = env['CM_MLPERF_INFERENCE_RNNT_PATH']
        cmd = "cd '" + env['RUN_DIR'] + "' && " + env['CM_PYTHON_BIN_WITH_PATH'] + " run.py --backend " + env['CM_MLPERF_BACKEND'] + \
                " --scenario " + env['CM_MLPERF_LOADGEN_SCENARIO'] + \
                " --manifest " + env['CM_DATASET_PREPROCESSED_JSON'] + \
                " --dataset_dir " + os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "..") + \
                " --pytorch_config_toml " + os.path.join("pytorch", "configs", "rnnt.toml") + \
                " --pytorch_checkpoint " + env['CM_ML_MODEL_FILE_WITH_PATH'] + \
                " --log_dir " + env['CM_MLPERF_OUTPUT_DIR'] + \
                env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options + dataset_options
        env['SKIP_VERIFY_ACCURACY'] = True

    elif "3d-unet" in env['CM_MODEL']:

        env['RUN_DIR'] = env['CM_MLPERF_INFERENCE_3DUNET_PATH']
        backend = env['CM_MLPERF_BACKEND'] if env['CM_MLPERF_BACKEND'] != 'tf' else 'tensorflow'
        cmd = "cd '" + env['RUN_DIR'] + "' && "+env['CM_PYTHON_BIN_WITH_PATH']+ " run.py --backend=" + backend + " --scenario="+env['CM_MLPERF_LOADGEN_SCENARIO'] + \
            env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + \
            " --model="+env['CM_ML_MODEL_FILE_WITH_PATH'] + \
            " --preprocessed_data_dir="+env['CM_DATASET_PREPROCESSED_PATH'] + \
            scenario_extra_options + mode_extra_options + dataset_options

        env['LOG_PATH'] = env['CM_MLPERF_OUTPUT_DIR']
        env['SKIP_VERIFY_ACCURACY'] = True

    elif "dlrm" in env['CM_MODEL']: # DLRM is in draft stage

        env['RUN_DIR'] = os.path.join(env['CM_MLPERF_INFERENCE_DLRM_PATH'], "..", "dlrm_v2", "pytorch")
        if 'terabyte' in env['CM_ML_MODEL_DATASET']:
            dataset = "terabyte"
        elif 'kaggle' in env['CM_ML_MODEL_DATASET']:
            dataset = "kaggle"
        elif 'multihot-criteo-sample' in env['CM_ML_MODEL_DATASET']:
            dataset = "multihot-criteo-sample"
        elif 'multihot-criteo' in env['CM_ML_MODEL_DATASET']:
            dataset = "multihot-criteo"

        if env.get('CM_MLPERF_BIN_LOADER', '') == 'yes':
            mlperf_bin_loader_string = " --mlperf-bin-loader"
        else:
            mlperf_bin_loader_string = ""
        if env.get('CM_ML_MODEL_DEBUG','') == 'yes':
            config = " --max-ind-range=10000000 --data-sub-sample-rate=0.875 "
        else:
            config = "  --max-ind-range=40000000 "

        if env['CM_MLPERF_DEVICE'] == "gpu":
            gpu_options = ""
            env['CUDA_VISIBLE_DEVICES'] = "0"
        else:
            gpu_options = ""
            env['WORLD_SIZE'] = "1"

        if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy" and env['CM_MLPERF_LOADGEN_SCENARIO'] == "Offline":
            mode_extra_options += " --samples-per-query-offline=1"

        cmd =  "cd '"+ env['RUN_DIR'] + "' && OUTPUT_DIR='" + env['CM_MLPERF_OUTPUT_DIR'] + "' ./run_local.sh " + env['CM_MLPERF_BACKEND'] + \
            ' dlrm ' + dataset + ' ' + env['CM_MLPERF_DEVICE'] + " --scenario " + env['CM_MLPERF_LOADGEN_SCENARIO'] + " " + \
            env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + \
            config + mlperf_bin_loader_string + \
            ' --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt ' + \
            scenario_extra_options + mode_extra_options + dataset_options + gpu_options
        cmd = cmd.replace("--count", "--count-queries")

    return cmd

def postprocess(i):

    env = i['env']

    if env.get('CM_MLPERF_README', "") == "yes":
        import cmind as cm
        inp = i['input']
        state = i['state']
        script_tags = inp['tags']
        script_adr = inp.get('add_deps_recursive', inp.get('adr', {}))

        cm_input = {'action': 'run',
                'automation': 'script',
                'tags': script_tags,
                'adr': script_adr,
                'env': env,
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
