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

    if env.get('CM_SYSTEM_POWER','') == "yes" or i['input'].get('power', '') == "yes":
        power = "yes"
    else:
        power = "no"
    rerun = env.get("CM_RERUN", "") or i['input'].get("rerun", False)
    required_files = []
    required_files = get_checker_files(env['CM_MLC_INFERENCE_SOURCE'])

    if env['CM_MODEL'] == "resnet50":
        cmd = "cp " + os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt") + " " + os.path.join(env['CM_DATASET_PATH'],
        "val_map.txt")
        ret = os.system(cmd)

    if 'CM_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_LOADGEN_EXTRA_OPTIONS'] = ""
    
    if 'CM_LOADGEN_MODES' not in env:
        if 'CM_LOADGEN_MODE' not in env:
            env['CM_LOADGEN_MODE'] = "performance"

    if 'CM_LOADGEN_SCENARIOS' not in env:
        if 'CM_LOADGEN_SCENARIO' not in env:
            env['CM_LOADGEN_SCENARIO'] = "Offline"

    if env.get('CM_LOADGEN_ALL_SCENARIOS', '') == "yes":
        system_meta = state['CM_SUT_META']
        env['CM_LOADGEN_SCENARIOS'] = get_valid_scenarios(env['CM_MODEL'], system_meta['system_type'], env['CM_MLC_LAST_RELEASE'], env['CM_MLC_INFERENCE_SOURCE'])
    else:
        system_meta = {}
        env['CM_LOADGEN_SCENARIOS'] = [ env['CM_LOADGEN_SCENARIO'] ]

    if env.get('CM_LOADGEN_ALL_MODES', '') == "yes":
        env['CM_LOADGEN_MODES'] = [ "performance", "accuracy" ]
    else:
        env['CM_LOADGEN_MODES'] = [ env['CM_LOADGEN_MODE'] ]

    if 'CM_LOADGEN_QPS' not in env:
        env['CM_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_LOADGEN_QPS_OPT'] = " --qps " + env['CM_LOADGEN_QPS']
    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_LOADGEN_QPS_OPT']

    if 'OUTPUT_BASE_DIR' not in env:
        env['OUTPUT_BASE_DIR'] = env['CM_MLC_INFERENCE_VISION_PATH']
    if 'output_dir' in i['input']:
        env['OUTPUT_BASE_DIR'] = i['input']['output_dir']

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_CPUINFO_CPUs']) // (int(env['CM_CPUINFO_Sockets']) * int(env['CM_CPUINFO_Threads_per_core']) ))
        else:
            env['CM_NUM_THREADS'] = str(int(env['CM_CPUINFO_CPUs']))


    if 'max-batchsize' in i['input']:
        env['CM_LOADGEN_EXTRA_OPTIONS'] += " --max-batchsize " + i['input']['max-batchsize']

    if 'count' in i['input']:
        env['CM_LOADGEN_EXTRA_OPTIONS'] += " --count " + i['input']['count']

    print("Using MLCommons Inference source from " + env['CM_MLC_INFERENCE_SOURCE'])

    if 'CM_MLC_MLPERF_CONF' not in env:
        env['CM_MLC_MLPERF_CONF'] = "'"+os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "mlperf.conf")+"'"


    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  " --mlperf_conf " + env['CM_MLC_MLPERF_CONF']

    env['DATA_DIR'] = env['CM_DATASET_PATH']
    env['MODEL_DIR'] = env['CM_ML_MODEL_PATH']

    env['RUN_DIR'] = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "vision", "classification_and_detection")
    RUN_CMDS = []
    COMPLIANCE_RUN_CMDS = []
    state['RUN'] = {}
    test_list = ["TEST01", "TEST04", "TEST05"]
    if env['CM_MODEL'] in ["rnnt", "bert-99", "bert-99.9", "dlrm-99", "dlrm-99.9", "3d-unet-99", "3d-unet-99.9"]:
        test_list.remove("TEST04")

    for scenario in env['CM_LOADGEN_SCENARIOS']:
        state['RUN'][scenario] = {}
        scenario_extra_options = ''

        NUM_THREADS = env['CM_NUM_THREADS']
        if scenario == "SingleStream":
            NUM_THREADS = "1"
        if scenario == "MultiStream":
            if int(env['CM_NUM_THREADS']) > 8:
                NUM_THREADS = "8"
        if 'threads' in i['input']: #input overrides everything
            NUM_THREADS = i['input']['threads']
        scenario_extra_options +=  " --threads " + NUM_THREADS

        conf = i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][scenario]
        user_conf = ''
        if ['CM_RUN_STYLE'] == "fast":
            fast_factor = env['CM_FAST_FACTOR'] 
        for metric in conf:
            metric_value = conf[metric]
            if env['CM_RUN_STYLE'] == "fast":
                if metric == "target_qps" and scenario == "Offline":
                    metric_value /= fast_factor
                if metric == "target_latency" and scenario in [ "SingleStream", "MultiStream" ]:
                    metric_value *= fast_factor
                conf[metric] = metric_value
            user_conf += env['CM_MODEL'] + "." + scenario + "." + metric + " = " + str(metric_value) + "\n"

        if env['CM_RUN_STYLE'] == "test":

            query_count = env['CM_TEST_QUERY_COUNT']
            user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
            if 'count' not in i['input']:
                scenario_extra_options +=  " --count " + query_count
        elif env['CM_RUN_STYLE'] == "fast":
            if scenario == "Server":
                target_qps = conf['target_qps']
                query_count = str((660/fast_factor)/(float(target_qps)))
                user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
                user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
                if 'count' not in i['input']:
                    scenario_extra_options +=  " --count " + query_count
        else:
            if scenario == "MultiStream":
                query_count = str(int((8000 / float(conf['target_latency'])) * 660))
                user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
                user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
                if 'count' not in i['input']:
                    scenario_extra_options +=  " --count " + query_count
        print(user_conf)
        import uuid
        key = uuid.uuid4().hex
        user_conf_path = os.path.join(script_path, "tmp", key+".conf")
        from pathlib import Path
        user_conf_file = Path(user_conf_path)
        user_conf_file.parent.mkdir(exist_ok=True, parents=True)
        user_conf_file.write_text(user_conf)
        scenario_extra_options +=  " --user_conf '" + user_conf_path + "'"

        env['CM_MLC_RESULTS_DIR'] = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])
        for mode in env['CM_LOADGEN_MODES']:
            mode_extra_options = ""
            OUTPUT_DIR =  os.path.join(env['CM_MLC_RESULTS_DIR'],
                        env['CM_BACKEND'] + "-" + env['CM_DEVICE'], env['CM_MODEL'], scenario.lower(),
                        mode)
            if mode == "accuracy":
                mode_extra_options += " --accuracy"
            elif mode == "performance":
                OUTPUT_DIR = os.path.join(OUTPUT_DIR, "run_1")
            print("Output Dir:" + OUTPUT_DIR)

            cmd =  "cd '"+ env['RUN_DIR'] + "' && OUTPUT_DIR='" + OUTPUT_DIR + "' ./run_local.sh " + env['CM_BACKEND'] + ' ' + env['CM_MODEL'] + ' ' + env['CM_DEVICE'] + " --scenario " + scenario + " " + env['CM_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options 
            if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun:
                RUN_CMDS.append(cmd)
            else:
                print("Run files exist, skipping run...\n")
            if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun or not measure_files_exist(OUTPUT_DIR,
                    required_files[4]) or env.get("CM_LOADGEN_COMPLIANCE", "") == "yes":
                state['RUN'][scenario][mode] = { "CM_MLC_RUN_CMD": cmd, "OUTPUT_DIR": OUTPUT_DIR, "CM_MLC_USER_CONF": user_conf_path }
            else:
                print("Measure files exist, skipping regeneration...\n")
        if system_meta.get('division', '') == "open":
            env["CM_LOADGEN_COMPLIANCE"] = "no" #no compliance runs needed for open division
        if env.get("CM_LOADGEN_COMPLIANCE", "") == "yes":
            for test in test_list:
                if test == "TEST01":
                    audit_path = os.path.join(test, env['CM_MODEL'])
                else:
                    audit_path = test
                audit_full_path = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "compliance", audit_path, "audit.config")
                mode_extra_options = " --audit " + audit_full_path
                OUTPUT_DIR =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'],
                        env['CM_BACKEND'] + "-" + env['CM_DEVICE'], env['CM_MODEL'], scenario.lower(),
                        test)
                print("Compliance Output Dir:" + OUTPUT_DIR)
                cmd =  "cd "+ env['RUN_DIR'] + " && OUTPUT_DIR=" + OUTPUT_DIR + " ./run_local.sh " + env['CM_BACKEND'] + ' ' + env['CM_MODEL'] + ' ' + env['CM_DEVICE'] + " --scenario " + scenario + " " + env['CM_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options + mode_extra_options
                if not run_files_exist("performance", OUTPUT_DIR, required_files) or rerun:
                    COMPLIANCE_RUN_CMDS.append(cmd)
                else:
                    print("Compliance run files exist, skipping compliance run...\n")
                    state['RUN'][scenario][test] = { "CM_MLC_RUN_CMD": cmd, "OUTPUT_DIR": OUTPUT_DIR, "CM_MLC_USER_CONF": user_conf_path }

    env['CM_MLC_RUN_CMDS'] = "??".join(RUN_CMDS)
    env['CM_MLC_COMPLIANCE_RUN_CMDS'] = "??".join(COMPLIANCE_RUN_CMDS)
    #print(state['RUN'])
    return {'return':0}

def run_files_exist(mode, OUTPUT_DIR, run_files):
    file_loc = {"accuracy": 0, "performance": 1, "power": 2, "performance_power": 3, "measure": 4}
    for file in run_files[file_loc[mode]]:
        if not os.path.exists(os.path.join(OUTPUT_DIR, file)) and file != "accuracy.txt":
            return False
    return True

def measure_files_exist(OUTPUT_DIR, run_files):
    for file in run_files:
        if not os.path.exists(os.path.join(OUTPUT_DIR, file)):
            return False
    return True

def get_valid_scenarios(model, category, mlc_version, mlc_path):
    import sys
    submission_checker_dir = os.path.join(mlc_path, "tools", "submission")
    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))
    import submission_checker as checker
    config = checker.MODEL_CONFIG
    internal_model_name = config[mlc_version]["model_mapping"][model]
    valid_scenarios = config[mlc_version]["required-scenarios-"+category][internal_model_name]
    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))
    return valid_scenarios

def get_checker_files(mlc_path):
    import sys
    submission_checker_dir = os.path.join(mlc_path, "tools", "submission")
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
    state = i['state']
    accuracy_results_dir = []
    model = env['CM_MODEL']
    if model == "resnet50":
        accuracy_filename = "accuracy-imagenet.py"
        dataset_args = " --imagenet-val-file " + \
        os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")
    elif model == "retinanet":
        accuracy_filename = "accuracy-openimages.py"
        dataset_args = " --openimages-dir " + env['CM_DATASET_PATH']

    for scenario in state['RUN']:
        for mode in state['RUN'][scenario]:
            if mode in [ "performance", "accuracy" ]:
                measurements = {}
                measurements['starting_weights_filename'] = env.get('CM_STARTING_WEIGHTS_FILENAME', 'none')
                measurements['retraining'] = env.get('MODEL_RETRAINING','')
                measurements['input_data_types'] = env.get('MODEL_INPUT_DATA_TYPES', 'fp32')
                measurements['weight_data_types'] = env.get('MODEL_WEIGHT_DATA_TYPES', 'fp32')
                measurements['weight_transformations'] = env.get('MODEL_WEIGHT_TRANSFORMATIONS', 'none')
                run = state['RUN'][scenario][mode]
                os.chdir(run['OUTPUT_DIR'])
                if mode == "accuracy":
                    '''
                    CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_VISION_PATH'], "tools", \
                    accuracy_filename) + " --mlperf-accuracy-file " + \
                    "mlperf_log_accuracy.json" + dataset_args + " > " + \
                    os.path.join(run['OUTPUT_DIR'], "accuracy.txt")
                    print(CMD)
                    result  = subprocess.run(CMD, shell=True)
                    '''
                    accuracy_results_dir.append(run['OUTPUT_DIR'])
                with open ("measurements.json", "w") as fp:
                    json.dump(measurements, fp, indent=2)
                if os.path.exists(env['CM_MLC_MLPERF_CONF']):
                    shutil.copy(env['CM_MLC_MLPERF_CONF'], 'mlperf.conf')
                if os.path.exists(run['CM_MLC_USER_CONF']):
                    shutil.copy(run['CM_MLC_USER_CONF'], 'user.conf')
                readme_init = ""
                readme_body = "##\n```\n" + run['CM_MLC_RUN_CMD'] + "\n```"
                readme = readme_init + readme_body
                with open ("README.md", "w") as fp:
                    fp.write(readme)
            elif mode in [ "TEST01", "TEST04", "TEST05" ]:
                compliance_run = state["RUN"][scenario][mode]
                RESULT_DIR = os.path.split(state['RUN'][scenario]["accuracy"]["OUTPUT_DIR"])[0]
                COMPLIANCE_DIR = compliance_run["OUTPUT_DIR"]
                split = os.path.split(RESULT_DIR)
                split = os.path.split(split[0])
                model = split[1]
                split = os.path.split(split[0])
                sut = split[1]
                split = os.path.split(split[0])
                OUTPUT_DIR = os.path.join(split[0], "compliance", sut, model, scenario)
                SCRIPT_PATH = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "compliance", "nvidia", mode, "run_verification.py")
                cmd = env['CM_PYTHON_BIN'] + " " + SCRIPT_PATH + " -r " + RESULT_DIR + " -c " + COMPLIANCE_DIR + " -o "+ OUTPUT_DIR
                os.system(cmd)
                if mode == "TEST01":
                    SCRIPT_PATH = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "compliance", "nvidia", mode,
                            "create_accuracy_baseline.sh")
                    ACCURACY_DIR = state['RUN'][scenario]["accuracy"]["OUTPUT_DIR"]
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
                        CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_VISION_PATH'], "tools", \
                                accuracy_filename) + " --mlperf-accuracy-file " + \
                                "mlperf_log_accuracy_baseline.json" + dataset_args + " > " + \
                                os.path.join(OUTPUT_DIR, "baseline_accuracy.txt")
                        print(CMD)
                        result  = subprocess.run(CMD, shell=True)
                        CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_VISION_PATH'], "tools", \
                                accuracy_filename) + " --mlperf-accuracy-file " + \
                                "mlperf_log_accuracy.json" + dataset_args + " > " + \
                                os.path.join(OUTPUT_DIR, "compliance_accuracy.txt")
                        print(CMD)
                        result  = subprocess.run(CMD, shell=True)


            else:
                print(mode)
    if len(accuracy_results_dir) > 0:
        env['CM_MLC_ACCURACY_RESULTS_DIR'] = ":".join(accuracy_results_dir)

    return {'return':0}
