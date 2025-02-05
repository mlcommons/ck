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
        return {'return': 0}

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes":
        return {'return': 0}

    if env.get('CM_MLPERF_POWER', '') == "yes":
        power = "yes"
    else:
        power = "no"

    rerun = True if env.get("CM_RERUN", "") != '' else False

    if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
        env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if 'CM_MLPERF_LOADGEN_MODE' not in env:
        env['CM_MLPERF_LOADGEN_MODE'] = "accuracy"

    if 'CM_MODEL' not in env:
        return {
            'return': 1, 'error': "Please select a variation specifying the model to run"}

    # if env['CM_MODEL'] == "resnet50":
    #    cmd = "cp " + os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt") + " " + os.path.join(env['CM_DATASET_PATH'],
    #    "val_map.txt")
    #    ret = os.system(cmd)

    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] = " " + \
        env.get('CM_MLPERF_LOADGEN_EXTRA_OPTIONS', '') + " "

    if 'CM_MLPERF_LOADGEN_QPS' not in env:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = " --qps " + \
            env['CM_MLPERF_LOADGEN_QPS']

    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += env['CM_MLPERF_LOADGEN_QPS_OPT']

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_HOST_CPU_TOTAL_CORES']) //
                                        (int(env.get('CM_HOST_CPU_SOCKETS', '1')) * int(env.get('CM_HOST_CPU_TOTAL_CORES', '1'))))
        else:
            env['CM_NUM_THREADS'] = env.get('CM_HOST_CPU_TOTAL_CORES', '1')

    if env.get('CM_MLPERF_LOADGEN_MAX_BATCHSIZE', '') != '' and not env.get(
            'CM_MLPERF_MODEL_SKIP_BATCHING', False):
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --max-batchsize " + \
            str(env['CM_MLPERF_LOADGEN_MAX_BATCHSIZE'])

    if env.get('CM_MLPERF_LOADGEN_BATCH_SIZE', '') != '':
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --batch-size " + \
            str(env['CM_MLPERF_LOADGEN_BATCH_SIZE'])

    if env.get('CM_MLPERF_LOADGEN_QUERY_COUNT', '') != '' and not env.get(
            'CM_TMP_IGNORE_MLPERF_QUERY_COUNT', False) and env.get('CM_MLPERF_RUN_STYLE', '') != "valid":
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --count " + \
            env['CM_MLPERF_LOADGEN_QUERY_COUNT']

    print("Using MLCommons Inference source from '" +
          env['CM_MLPERF_INFERENCE_SOURCE'] + "'")

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(
            env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")

    x = "" if os_info['platform'] == 'windows' else "'"
    if "llama2-70b" in env['CM_MODEL']:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --mlperf-conf " + \
            x + env['CM_MLPERF_CONF'] + x
    else:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --mlperf_conf " + \
            x + env['CM_MLPERF_CONF'] + x

    env['MODEL_DIR'] = env.get('CM_ML_MODEL_PATH')
    if not env['MODEL_DIR']:
        env['MODEL_DIR'] = os.path.dirname(
            env.get(
                'CM_MLPERF_CUSTOM_MODEL_PATH',
                env.get('CM_ML_MODEL_FILE_WITH_PATH')))

    RUN_CMD = ""

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    scenario_extra_options = ''

    NUM_THREADS = env['CM_NUM_THREADS']
    if int(NUM_THREADS) > 2 and env['CM_MLPERF_DEVICE'] == "gpu":
        NUM_THREADS = "2"  # Don't use more than 2 threads when run on GPU

    if env['CM_MODEL'] in ['resnet50', 'retinanet', 'stable-diffusion-xl']:
        scenario_extra_options += " --threads " + NUM_THREADS

    ml_model_name = env['CM_MODEL']
    if 'CM_MLPERF_USER_CONF' in env:
        user_conf_path = env['CM_MLPERF_USER_CONF']
        x = "" if os_info['platform'] == 'windows' else "'"
        scenario_extra_options += " --user_conf " + x + user_conf_path + x

    mode = env['CM_MLPERF_LOADGEN_MODE']
    mode_extra_options = ""

    # Grigori blocked for ABTF to preprocess data set on the fly for now
    # we can later move it to a separate script to preprocess data set

#    if 'CM_DATASET_PREPROCESSED_PATH' in env and env['CM_MODEL'] in  [ 'resnet50', 'retinanet' ]:
#        #dataset_options = " --use_preprocessed_dataset --preprocessed_dir "+env['CM_DATASET_PREPROCESSED_PATH']
#        if env.get('CM_MLPERF_LAST_RELEASE') not in [ "v2.0", "v2.1" ]:
#            dataset_options = " --use_preprocessed_dataset --cache_dir "+env['CM_DATASET_PREPROCESSED_PATH']
#        else:
#            dataset_options = ""
#        if env['CM_MODEL'] == "retinanet":
#            dataset_options += " --dataset-list "+ env['CM_DATASET_ANNOTATIONS_FILE_PATH']
#        elif env['CM_MODEL'] == "resnet50":
#            dataset_options += " --dataset-list "+ os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")
#        env['DATA_DIR'] = env.get('CM_DATASET_PREPROCESSED_PATH')
#    else:
#        if 'CM_DATASET_PREPROCESSED_PATH' in env:
#            env['DATA_DIR'] = env.get('CM_DATASET_PREPROCESSED_PATH')
#        else:
#            env['DATA_DIR'] = env.get('CM_DATASET_PATH')
#        dataset_options = ''

    # Grigori added for ABTF
#    dataset_path = env.get('CM_DATASET_PATH')
#    env['DATA_DIR'] = dataset_path

#    dataset_options = " --dataset-list " + env['CM_DATASET_ANNOTATIONS_FILE_PATH']
#    dataset_options += " --cache_dir " + os.path.join(script_path, 'preprocessed-dataset')

    dataset_options = ''

    if env.get('CM_MLPERF_EXTRA_DATASET_ARGS', '') != '':
        dataset_options += " " + env['CM_MLPERF_EXTRA_DATASET_ARGS']

    if mode == "accuracy":
        mode_extra_options += " --accuracy"
        env['CM_OUTPUT_PREDICTIONS_PATH'] = os.path.join(
            env['CM_DATASET_MLCOMMONS_COGNATA_PATH'],
            env['CM_DATASET_MLCOMMONS_COGNATA_SERIAL_NUMBERS'],
            'Cognata_Camera_01_8M_png',
            'output')

    elif mode == "performance":
        pass

    elif mode == "compliance":

        audit_full_path = env['CM_MLPERF_INFERENCE_AUDIT_PATH']
        mode_extra_options = " --audit '" + audit_full_path + "'"

    if env.get('CM_MLPERF_OUTPUT_DIR', '') == '':
        env['CM_MLPERF_OUTPUT_DIR'] = os.getcwd()

    mlperf_implementation = env.get('CM_MLPERF_IMPLEMENTATION', 'reference')

    # Generate CMD

    # Grigori updated for ABTF demo
#    cmd, run_dir = get_run_cmd(os_info, env, scenario_extra_options, mode_extra_options, dataset_options, mlperf_implementation)
    cmd, run_dir = get_run_cmd_reference(
        os_info, env, scenario_extra_options, mode_extra_options, dataset_options, script_path)

    if env.get('CM_NETWORK_LOADGEN', '') == "lon":

        run_cmd = i['state']['mlperf_inference_run_cmd']
        env['CM_SSH_RUN_COMMANDS'] = []
        env['CM_SSH_RUN_COMMANDS'].append(
            run_cmd.replace(
                "--network=lon",
                "--network=sut") + " &")

    env['CM_MLPERF_RUN_CMD'] = cmd
    env['CM_RUN_DIR'] = run_dir
    env['CM_RUN_CMD'] = cmd
    env['CK_PROGRAM_TMP_DIR'] = env.get('CM_ML_MODEL_PATH')  # for tvm

    if env.get('CM_HOST_PLATFORM_FLAVOR', '') == "arm64":
        env['CM_HOST_PLATFORM_FLAVOR'] = "aarch64"

    if not env.get('CM_COGNATA_ACCURACY_DUMP_FILE'):
        env['CM_COGNATA_ACCURACY_DUMP_FILE'] = os.path.join(
            env['OUTPUT_DIR'], "accuracy.txt")

    return {'return': 0}


def get_run_cmd_reference(os_info, env, scenario_extra_options,
                          mode_extra_options, dataset_options, script_path=None):

    q = '"' if os_info['platform'] == 'windows' else "'"

    ##########################################################################
    # Grigori added for ABTF demo

    if env['CM_MODEL'] in ['retinanet']:

        run_dir = os.path.join(script_path, 'ref')

        env['RUN_DIR'] = run_dir

        env['OUTPUT_DIR'] = env['CM_MLPERF_OUTPUT_DIR']

        cognata_dataset_path = env['CM_DATASET_MLCOMMONS_COGNATA_PATH']
# cognata_dataset_path = env['CM_DATASET_PATH'] # Using open images
# dataset for some tests

        path_to_model = env.get(
            'CM_MLPERF_CUSTOM_MODEL_PATH',
            env.get(
                'CM_ML_MODEL_FILE_WITH_PATH',
                env.get('CM_ML_MODEL_CODE_WITH_PATH')))
        env['MODEL_FILE'] = path_to_model

        cmd = env['CM_PYTHON_BIN_WITH_PATH'] + " " + os.path.join(run_dir, "python", "main.py") + " --profile " + env['CM_MODEL'] + "-" + env['CM_MLPERF_BACKEND'] + \
            " --model=" + q + path_to_model + q + \
            " --dataset=" + env["CM_MLPERF_VISION_DATASET_OPTION"] + \
            " --dataset-path=" + q + cognata_dataset_path + q + \
            " --cache_dir=" + q + os.path.join(script_path, 'tmp-preprocessed-dataset') + q + \
            " --scenario " + env['CM_MLPERF_LOADGEN_SCENARIO'] + " " + \
            " --output " + q + env['OUTPUT_DIR'] + q + " " + \
            env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] + \
            scenario_extra_options + mode_extra_options + dataset_options

    ##########################################################################

    return cmd, run_dir


def postprocess(i):

    env = i['env']

    state = i['state']

    inp = i['input']

    return {'return': 0}
