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

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    if env.get('CM_SYSTEM_POWER','') == "yes":
        power = "yes"
    else:
        power = "no"

    rerun = True if env.get("CM_RERUN","")!='' else False

    required_files = []
    required_files = get_checker_files(env['CM_MLPERF_INFERENCE_SOURCE'])

    if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
        env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if 'CM_MLPERF_LOADGEN_MODE' not in env:
        env['CM_MLPERF_LOADGEN_MODE'] = "accuracy"

    if 'CM_MLPERF_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] = ""

    if 'CM_MLPERF_LOADGEN_QPS' not in env:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_MLPERF_LOADGEN_QPS_OPT'] = " --qps " + env['CM_MLPERF_LOADGEN_QPS']

    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_MLPERF_LOADGEN_QPS_OPT']

    if 'OUTPUT_BASE_DIR' not in env:
        env['OUTPUT_BASE_DIR'] = os.getcwd()

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_HOST_CPU_TOTAL_CORES']) // \
                    (int(env.get('CM_HOST_CPU_SOCKETS', '1')) * int(env.get('CM_HOST_CPU_TOTAL_CORES', '1'))))
        else:
            env['CM_NUM_THREADS'] = env.get('CM_HOST_CPU_TOTAL_CORES', '1')


    if 'CM_MLPERF_LOADGEN_MAX_BATCHSIZE' in env:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --max-batchsize " + env['CM_MLPERF_LOADGEN_MAX_BATCHSIZE']

    if 'CM_MLPERF_LOADGEN_QUERY_COUNT' in env:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] += " --count " + env['CM_MLPERF_LOADGEN_QUERY_COUNT']

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")


    env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] +=  " --mlperf_conf '" + env['CM_MLPERF_CONF'] + "'"


    RUN_CMD = ""
    state['RUN'] = {}
    test_list = ["TEST01", "TEST04", "TEST05"]
    if env['CM_MODEL'] in ["rnnt", "bert-99", "bert-99.9", "dlrm-99", "dlrm-99.9", "3d-unet-99", "3d-unet-99.9"]:
        test_list.remove("TEST04")

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    state['RUN'][scenario] = {}
    scenario_extra_options = ''

    NUM_THREADS = env['CM_NUM_THREADS']
    if scenario == "SingleStream":
        NUM_THREADS = "1"
    if scenario == "MultiStream":
        if int(env['CM_NUM_THREADS']) > 8:
            NUM_THREADS = "8"

    if "bert" not in env['CM_MODEL']:
        scenario_extra_options +=  " --threads " + NUM_THREADS

    if env['CM_MODEL'] not in i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']]:
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']] = {}
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][scenario] = {}


    conf = i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][scenario]
    user_conf = ''
    if ['CM_MLPERF_RUN_STYLE'] == "fast":
        fast_factor = env['CM_FAST_FACTOR']
    else:
        fast_factor = 1
    ml_model_name = env['CM_MODEL']
    if 'bert' in ml_model_name:
        ml_model_name = "bert"
    if 'dlrm' in ml_model_name:
        ml_model_name = "dlrm"

    query_count = None

    value = None
    if scenario in [ 'Offline', 'Server' ]:
        metric = "target_qps"
        #value = env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS') if scenario == "Server" else env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS')
        if not value:
            value = env.get('CM_MLPERF_LOADGEN_TARGET_QPS')
    elif scenario in [ 'SingleStream', 'MultiStream' ]:
        metric = "target_latency"
        if not value:
            value = env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY')

    if value:
        metric_value = value
        conf[metric] = value
    else:
        if metric in conf:
            metric_value = conf[metric]
        else:
            return {'return': 1, 'error': f"Config details missing for SUT:{env['CM_SUT_NAME']}, Model:{env['CM_MODEL']}, Scenario: {scenario}. Please input {metric} value"}

    if env['CM_MLPERF_RUN_STYLE'] == "fast":
        if scenario == "Offline":
            metric_value /= fast_factor
        if scenario in [ "SingleStream", "MultiStream" ]:
            metric_value *= fast_factor
    elif env['CM_MLPERF_RUN_STYLE'] == "test":
        if scenario == "Offline":
            metric_value = 1
        if scenario in [ "SingleStream" ]:
            metric_value = 1000
    conf[metric] = metric_value
    user_conf += ml_model_name + "." + scenario + "." + metric + " = " + str(metric_value) + "\n"

    if env['CM_MLPERF_RUN_STYLE'] == "test":
        query_count = env.get('CM_TEST_QUERY_COUNT', "5")
        user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
        user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
        user_conf += ml_model_name + "." + scenario + ".min_duration = 0" + "\n"
        scenario_extra_options +=  " --count " + query_count

    elif env['CM_MLPERF_RUN_STYLE'] == "fast":
        if scenario == "Server":
            target_qps = conf['target_qps']
            query_count = str((660/fast_factor)/(float(target_qps)))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_duration = 0" + "\n"
            scenario_extra_options +=  " --count " + query_count
    else:
        if scenario == "MultiStream":
            query_count = str(int((8000 / float(conf['target_latency'])) * 660))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
            scenario_extra_options +=  " --count " + query_count

    if query_count:
        env['CM_MAX_EXAMPLES'] = query_count #needed for squad accuracy checker

    import uuid
    key = uuid.uuid4().hex
    user_conf_path = os.path.join(script_path, "tmp", key+".conf")
    from pathlib import Path
    user_conf_file = Path(user_conf_path)
    user_conf_file.parent.mkdir(exist_ok=True, parents=True)
    user_conf_file.write_text(user_conf)
    if 'CM_MLPERF_LOADGEN_QUERY_COUNT' not in env and query_count:
        env['CM_MLPERF_LOADGEN_QUERY_COUNT'] = query_count

    scenario_extra_options +=  " --user_conf '" + user_conf_path + "'"

    env['CM_MLPERF_RESULTS_DIR'] = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])

    mode = env['CM_MLPERF_LOADGEN_MODE']
    mode_extra_options = ""
    if 'CM_DATASET_PREPROCESSED_PATH' in env:
        dataset_options = " --cache_dir "+env['CM_DATASET_PREPROCESSED_PATH']
    else:
        dataset_options = ''
    OUTPUT_DIR =  os.path.join(env['CM_MLPERF_RESULTS_DIR'], env['CM_MLPERF_BACKEND'] + "-" + env['CM_MLPERF_DEVICE'], \
            env['CM_MODEL'], scenario.lower(), mode)
    if mode == "accuracy":
        mode_extra_options += " --accuracy"
    elif mode == "performance":
        OUTPUT_DIR = os.path.join(OUTPUT_DIR, "run_1")
    elif mode == "compliance":
        test = env.get("CM_MLPERF_LOADGEN_COMPIANCE_TEST", "TEST01")
        OUTPUT_DIR =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'], env['CM_MLPERF_BACKEND'] \
                + "-" + env['CM_MLPERF_DEVICE'], env['CM_MODEL'], scenario.lower(), test)
        if test == "TEST01":
            audit_path = os.path.join(test, env['CM_MODEL'])
        else:
            audit_path = test

        audit_full_path = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", audit_path, "audit.config")
        mode_extra_options = " --audit '" + audit_full_path + "'"
    env['CM_MLPERF_OUTPUT_DIR'] = OUTPUT_DIR
    env['CM_MLPERF_LOADGEN_LOGS_DIR'] = OUTPUT_DIR
    
    if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun:
        print("Output Dir: '" + OUTPUT_DIR + "'")
        print(user_conf)
    else:
        print("Run files exist, skipping run...\n")
        env['CM_SKIP_RUN'] = "yes"

    if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun or not measure_files_exist(OUTPUT_DIR, \
                    required_files[4]) or env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes" or env.get("CM_REGENERATE_MEASURE_FILES", False):
        env['CM_MLPERF_USER_CONF'] = user_conf_path
    else:
        print("Measure files exist, skipping regeneration...\n")
        env['CM_MLPERF_USER_CONF'] = ''
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    return {'return':0}

def run_files_exist(mode, OUTPUT_DIR, run_files):
    file_loc = {"accuracy": 0, "performance": 1, "power": 2, "performance_power": 3, "measure": 4}
    for file in run_files[file_loc[mode]]:
        file_path = os.path.join(OUTPUT_DIR, file)
        if not os.path.exists(file_path) and file != "accuracy.txt":
            return False
    return True

def measure_files_exist(OUTPUT_DIR, run_files):
    for file in run_files:
        file_path = os.path.join(OUTPUT_DIR, file)
        if not os.path.exists(file_path):
            return False
    return True

def get_valid_scenarios(model, category, mlperf_version, mlperf_path):
    import sys
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))
    import submission_checker as checker
    config = checker.MODEL_CONFIG
    internal_model_name = config[mlperf_version]["model_mapping"][model]
    valid_scenarios = config[mlperf_version]["required-scenarios-"+category][internal_model_name]
    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))
    return valid_scenarios

def get_checker_files(mlperf_path):
    import sys
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))
    import submission_checker as checker
    REQUIRED_ACC_FILES = checker.REQUIRED_ACC_FILES
    REQUIRED_PERF_FILES = checker.REQUIRED_PERF_FILES
    REQUIRED_POWER_FILES = checker.REQUIRED_POWER_FILES
    REQUIRED_MEASURE_FILES = checker.REQUIRED_MEASURE_FILES
    REQUIRED_PERF_POWER_FILES = checker.REQUIRED_PERF_POWER_FILES
    return REQUIRED_ACC_FILES, REQUIRED_PERF_FILES, REQUIRED_POWER_FILES, REQUIRED_PERF_POWER_FILES, REQUIRED_MEASURE_FILES


def postprocess(i):
    env = i['env']
    inp = i['input']
    state = i['state']
    if env['CM_MLPERF_USER_CONF'] == '':
        return {'return': 0}
    output_dir = env['CM_MLPERF_OUTPUT_DIR']
    accuracy_result_dir = ''
    model = env['CM_MODEL']
    if model == "resnet50":
        accuracy_filename = "accuracy-imagenet.py"
        dataset_args = " --imagenet-val-file " + \
        os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")
    elif model == "retinanet":
        accuracy_filename = "accuracy-openimages.py"
        dataset_args = " --openimages-dir " + env['CM_DATASET_PATH']

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    mode = env['CM_MLPERF_LOADGEN_MODE']
    if mode in [ "performance", "accuracy" ]:
        measurements = {}
        measurements['starting_weights_filename'] = env.get('CM_ML_MODEL_STARTING_WEIGHTS_FILENAME', 'none')
        measurements['retraining'] = env.get('MODEL_RETRAINING','')
        measurements['input_data_types'] = env.get('CM_ML_MODEL_INPUT_DATA_TYPES', 'fp32')
        measurements['weight_data_types'] = env.get('CM_ML_MODEL_WEIGHT_DATA_TYPES', 'fp32')
        measurements['weight_transformations'] = env.get('CM_ML_MODEL_WEIGHT_TRANSFORMATIONS', 'none')
        os.chdir(output_dir)
        if not os.path.exists("mlperf_log_summary.txt"):
            return {'return': 0}
        print("\n")
        with open("mlperf_log_summary.txt", "r") as fp:
            print(fp.read())

        if mode == "accuracy":
            accuracy_result_dir = output_dir
        with open ("measurements.json", "w") as fp:
            json.dump(measurements, fp, indent=2)
        if os.path.exists(env['CM_MLPERF_CONF']):
            shutil.copy(env['CM_MLPERF_CONF'], 'mlperf.conf')
        if os.path.exists(env['CM_MLPERF_USER_CONF']):
            shutil.copy(env['CM_MLPERF_USER_CONF'], 'user.conf')
        if "cmd" in inp:
            cmd = "cm run script \\\n\t"+" \\\n\t".join(inp['cmd'])
        else:
            cmd = ""
        readme_init = "This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)\n"
        readme_body = "## CM Run Command\n```\n" + cmd + "\n```"
        readme = readme_init + readme_body
        with open ("README.md", "w") as fp:
            fp.write(readme)
    elif mode in [ "TEST01", "TEST04", "TEST05" ]:
        RESULT_DIR = os.path.split(output_dir)[0]
        COMPLIANCE_DIR = output_dir
        split = os.path.split(RESULT_DIR)
        split = os.path.split(split[0])
        model = split[1]
        split = os.path.split(split[0])
        sut = split[1]
        split = os.path.split(split[0])
        OUTPUT_DIR = os.path.join(split[0], "compliance", sut, model, scenario)
        SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", mode, "run_verification.py")
        cmd = env['CM_PYTHON_BIN'] + " " + SCRIPT_PATH + " -r " + RESULT_DIR + " -c " + COMPLIANCE_DIR + " -o "+ OUTPUT_DIR
        os.system(cmd)
        if mode == "TEST01":
            SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", mode,
                    "create_accuracy_baseline.sh")
            ACCURACY_DIR = os.path.join(RESULT_DIR, "accuracy")
            if (os.path.exists(ACCURACY_DIR)):
                print("Accuracy run not yet completed")
                return {'return':1}
            cmd = "bash " + SCRIPT_PATH + " " + os.path.join(ACCURACY_DIR, "mlperf_log_accuracy.json") + " " + \
                    os.path.join(COMPLIANCE_DIR, "mlperf_log_accuracy.json")
            print(cmd)
            result  = subprocess.run(cmd, shell=True)
            CMD = "cat verify_accuracy.txt | grep 'TEST PASS'"
            result  = subprocess.check_output(CMD, shell=True).decode("utf-8")
            if not result: #Normal test failed, trying the check with non-determinism

                OUTPUT_DIR = os.path.join(OUTPUT_DIR, "TEST01", "accuracy")
                if not os.path.exists(OUTPUT_DIR):
                    os.makedirs(OUTPUT_DIR)
                CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                        accuracy_filename) + " --mlperf-accuracy-file " + \
                        "mlperf_log_accuracy_baseline.json" + dataset_args + " > " + \
                        os.path.join(OUTPUT_DIR, "baseline_accuracy.txt")
                print(CMD)
                result  = subprocess.run(CMD, shell=True)
                CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                        accuracy_filename) + " --mlperf-accuracy-file " + \
                        "mlperf_log_accuracy.json" + dataset_args + " > " + \
                        os.path.join(OUTPUT_DIR, "compliance_accuracy.txt")
                print(CMD)
                result  = subprocess.run(CMD, shell=True)

    else:
        print(mode)

    if accuracy_result_dir != '':
        env['CM_MLPERF_ACCURACY_RESULTS_DIR'] = accuracy_result_dir

    return {'return':0}
