from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm
import sys

def preprocess(i):


    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    rerun = True if env.get("CM_RERUN","")!='' else False

    env['CM_MLPERF_SKIP_RUN'] = env.get('CM_MLPERF_SKIP_RUN', "no")

    mlperf_path = env['CM_MLPERF_INFERENCE_SOURCE']
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)

    version = env.get('CM_MLPERF_INFERENCE_VERSION', "4.0")

    required_files = []
    required_files = get_checker_files()

    if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
        env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if 'CM_MLPERF_LOADGEN_MODE' not in env:
        print("\nNo mode given. Using accuracy as default\n")
        env['CM_MLPERF_LOADGEN_MODE'] = "accuracy"


    if env.get('OUTPUT_BASE_DIR', '') == '':
        env['OUTPUT_BASE_DIR'] = env.get('CM_MLPERF_INFERENCE_RESULTS_DIR', os.getcwd())

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_HOST_CPU_TOTAL_CORES']) // \
                    (int(env.get('CM_HOST_CPU_SOCKETS', '1')) * int(env.get('CM_HOST_CPU_TOTAL_CORES', '1'))))
        else:
            env['CM_NUM_THREADS'] = env.get('CM_HOST_CPU_TOTAL_CORES', '1')


    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    if 'CM_MLPERF_CONF' not in env:
        env['CM_MLPERF_CONF'] = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "mlperf.conf")


    RUN_CMD = ""
    state['RUN'] = {}
    test_list = ["TEST01", "TEST04", "TEST05"]
    if env['CM_MODEL'] in ["rnnt", "bert-99", "bert-99.9", "dlrm-v2-99", "dlrm-v2-99.9", "3d-unet-99", "3d-unet-99.9"]:
        test_list.remove("TEST04")
    if "gpt-" in env['CM_MODEL']:
        test_list.remove("TEST05")
        test_list.remove("TEST04")
        test_list.remove("TEST01")

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    state['RUN'][scenario] = {}

    model_full_name = env.get('CM_ML_MODEL_FULL_NAME', env['CM_MODEL'])

    if model_full_name != env['CM_MODEL']:
        if 'model_mapping' not in state['CM_SUT_CONFIG']:
            state['CM_SUT_CONFIG']['model_mappings'] = {}
        state['CM_SUT_CONFIG']['model_mappings'][model_full_name] = env['CM_MODEL']

    if model_full_name not in i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']]:
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][model_full_name] = {}

    if scenario not in i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][model_full_name]:
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][model_full_name][scenario] = {}


    conf = i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][model_full_name][scenario]

    mode = env['CM_MLPERF_LOADGEN_MODE']

    user_conf = ''
    if env['CM_MLPERF_RUN_STYLE'] == "fast":
        fast_factor = int(env['CM_FAST_FACTOR'])
    else:
        fast_factor = 1

    ml_model_name = env['CM_MODEL']
    if 'bert' in ml_model_name:
        ml_model_name = "bert"
    if 'dlrm' in ml_model_name:
        ml_model_name = "dlrm-v2"
    if '3d-unet' in ml_model_name:
        ml_model_name = "3d-unet"
    if 'gptj' in ml_model_name:
        ml_model_name = "gptj"

    query_count = None

    value = None
    if scenario in [ 'Offline', 'Server' ]:
        metric = "target_qps"
        tolerance = 1.01
        #value = env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS') if scenario == "Server" else env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS')
        value = env.get('CM_MLPERF_LOADGEN_TARGET_QPS')
    elif scenario in [ 'SingleStream', 'MultiStream' ]:
        metric = "target_latency"
        value = env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY')
        if value:
            if scenario == "SingleStream" and (1000/float(value) * 660 < 100):
                env['CM_MLPERF_USE_MAX_DURATION'] = 'no'
            elif scenario == "MultiStream" and (1000/float(value) * 660 < 662):
                env['CM_MLPERF_USE_MAX_DURATION'] = 'no'
        if env.get('CM_MLPERF_MODEL_EQUAL_ISSUE_MODE', 'no').lower() not in [ "yes", "1", "true" ] and env.get('CM_MLPERF_USE_MAX_DURATION', "yes").lower() not in [ "no", "false", "0"]:
            tolerance = 0.4 #much lower because we have max_duration
        else:
            tolerance = 0.9
    else:
        return {'return': 1, 'error': 'Invalid scenario: {}'.format(scenario)}

    if value:
        metric_value = value
        conf[metric] = value
    else:
        if metric in conf:
            print("Original configuration value {} {}".format(conf[metric], metric))
            metric_value = str(float(conf[metric]) * tolerance) #some tolerance
            print("Adjusted configuration value {} {}".format(metric_value, metric))
        else:
            #if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes":
            if metric == "target_qps":
                if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes":
                    print("In find performance mode: using 1 as target_qps")
                else:
                    print("No target_qps specified. Using 1 as target_qps")
                conf[metric] = 1
            if metric == "target_latency":
                if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes":
                    print("In find performance mode: using 0.5ms as target_latency")
                else:
                    print("No target_latency specified. Using default")
                if env.get('CM_MLPERF_USE_MAX_DURATION', 'yes').lower() in [ "no", "false", "0" ] or env.get('CM_MLPERF_MODEL_EQUAL_ISSUE_MODE', 'no').lower() in [ "yes", "1", "true" ]:
                    # Total number of queries needed is a multiple of dataset size. So we dont use max_duration and so we need to be careful with the input latency
                    if '3d-unet' in env['CM_MODEL']:
                        conf[metric] = 400
                    elif 'gptj' in env['CM_MODEL']:
                        conf[metric] = 1000
                    else:
                        conf[metric] = 100
                else:
                    conf[metric] = 0.5
            metric_value = conf[metric]
            #else:
            #    return {'return': 1, 'error': f"Config details missing for SUT:{env['CM_SUT_NAME']}, Model:{env['CM_MODEL']}, Scenario: {scenario}. Please input {metric} value"}

    #Pass the modified performance metrics to the implementation
    if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes":
        if metric == "target_latency" and env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY', '') == '':
            env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = conf[metric]
        elif metric == "target_qps" and env.get('CM_MLPERF_LOADGEN_TARGET_QPS', '') == '':
            env['CM_MLPERF_LOADGEN_TARGET_QPS'] = conf[metric]


    if env['CM_MLPERF_RUN_STYLE'] == "fast":
        if scenario == "Offline":
            metric_value = float(metric_value) / fast_factor
        if scenario in [ "SingleStream", "MultiStream" ]:
            metric_value = float(metric_value) * fast_factor

    elif env['CM_MLPERF_RUN_STYLE'] == "test":
        if scenario == "Offline":
            metric_value = 1
        if scenario in [ "SingleStream" ]:
            metric_value = 1000

    elif env['CM_MLPERF_RUN_STYLE'] == "valid":
        if scenario == "Offline":
            required_min_queries_offline = {}
            required_min_queries_offline = get_required_min_queries_offline(env['CM_MODEL'], version)


        if  mode == "compliance" and scenario == "Server": #Adjust the server_target_qps
            test = env.get("CM_MLPERF_LOADGEN_COMPLIANCE_TEST", "TEST01")
            if test == "TEST01":
                metric_value = str(float(metric_value) * float(env.get("CM_MLPERF_TEST01_SERVER_ADJUST_FACTOR", 0.96)))
            if test == "TEST05":
                metric_value = str(float(metric_value) * float(env.get("CM_MLPERF_TEST05_SERVER_ADJUST_FACTOR", 0.97)))
            if test == "TEST04":
                metric_value = str(float(metric_value) * float(env.get("CM_MLPERF_TEST04_SERVER_ADJUST_FACTOR", 0.97)))

    conf[metric] = metric_value
    user_conf += ml_model_name + "." + scenario + "." + metric + " = " + str(metric_value) + "\n"

    if env.get('CM_MLPERF_PERFORMANCE_SAMPLE_COUNT', '') != '':
        performance_sample_count = env['CM_MLPERF_PERFORMANCE_SAMPLE_COUNT']
        user_conf += ml_model_name + ".*.performance_sample_count_override = " + performance_sample_count + "\n"

    log_mode = mode
    if 'CM_MLPERF_POWER' in env and mode == "performance":
        log_mode = "performance_power"

    env['CM_MLPERF_INFERENCE_FINAL_RESULTS_DIR'] = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])

    sut_name = env.get('CM_SUT_NAME', env['CM_MLPERF_BACKEND'] + "-" + env['CM_MLPERF_DEVICE'])
    OUTPUT_DIR =  os.path.join(env['CM_MLPERF_INFERENCE_FINAL_RESULTS_DIR'], sut_name, \
            model_full_name, scenario.lower(), mode)

    if 'CM_MLPERF_POWER' in env and mode == "performance":
        env['CM_MLPERF_POWER_LOG_DIR'] = os.path.join(OUTPUT_DIR, "tmp_power")

    if mode == "accuracy":
        pass
    elif mode == "performance":
        OUTPUT_DIR = os.path.join(OUTPUT_DIR, "run_1")
    elif mode == "compliance":
        test = env.get("CM_MLPERF_LOADGEN_COMPLIANCE_TEST", "TEST01")
        OUTPUT_DIR =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'], sut_name, model_full_name, scenario.lower(), test)
        if test == "TEST01":
            audit_path = os.path.join(test, ml_model_name)
        else:
            audit_path = test

        audit_full_path = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", audit_path, "audit.config")
        env['CM_MLPERF_INFERENCE_AUDIT_PATH'] = audit_full_path
        #copy the audit conf to the run directory incase the implementation is not supporting the audit-conf path
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        shutil.copyfile(audit_full_path, os.path.join(OUTPUT_DIR, "audit.config"))

    env['CM_MLPERF_OUTPUT_DIR'] = OUTPUT_DIR
    env['CM_LOGS_DIR'] = OUTPUT_DIR
    env['CM_MLPERF_LOADGEN_LOGS_DIR'] = OUTPUT_DIR

    if mode == "accuracy":
        output_dir = env['CM_MLPERF_OUTPUT_DIR']
        env['CM_MLPERF_ACCURACY_RESULTS_DIR'] = output_dir
    else:
        env['CM_MLPERF_ACCURACY_RESULTS_DIR'] = ''

    run_exists = run_files_exist(log_mode, OUTPUT_DIR, required_files, env)

    if 'CM_MLPERF_POWER' in env and env.get('CM_MLPERF_SHORT_RANGING_RUN', '') != 'no' and env['CM_MLPERF_RUN_STYLE'] == "valid" and mode == "performance":
        short_ranging = True
    else:
        short_ranging = False

    if short_ranging:
        import copy
        ranging_user_conf = copy.deepcopy(user_conf)
        ranging_user_conf += ml_model_name + "." + scenario + ".min_duration = 300000" + "\n"

    if env['CM_MLPERF_RUN_STYLE'] == "test":
        query_count = env.get('CM_TEST_QUERY_COUNT', "5")
        user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
        user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
        user_conf += ml_model_name + "." + scenario + ".min_duration = 0" + "\n"
        #else:
        #    user_conf += ml_model_name + "." + scenario + ".min_duration = 20000" + "\n"
        #    user_conf += ml_model_name + "." + scenario + ".max_duration = 20000 \n "

    elif env['CM_MLPERF_RUN_STYLE'] == "fast":
        if scenario == "Server":
            target_qps = conf['target_qps']
            query_count = str(int((660/fast_factor) * (float(target_qps))))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"

    else:
        if scenario == "MultiStream" or scenario == "SingleStream":
            if env.get('CM_MLPERF_USE_MAX_DURATION', 'yes').lower() not in [ "no", "false", "0" ] and env.get('CM_MLPERF_MODEL_EQUAL_ISSUE_MODE', 'no').lower() not in [ "yes", "1", "true" ]:
                user_conf += ml_model_name + "." + scenario + ".max_duration = 660000 \n"
            elif env.get('CM_MLPERF_INFERENCE_MIN_DURATION','') != '':
                user_conf += ml_model_name + "." + scenario + ".min_duration = " + env['CM_MLPERF_INFERENCE_MIN_DURATION'] +" \n"
            if scenario == "MultiStream":
                user_conf += ml_model_name + "." + scenario + ".min_query_count = "+ env.get('CM_MLPERF_INFERENCE_MULTISTREAM_MIN_QUERY_COUNT', "662") + "\n"
            if short_ranging:
                ranging_user_conf += ml_model_name + "." + scenario + ".max_duration = 300000 \n "
        elif scenario == "SingleStream_old":
            query_count = str(max(int((1000 / float(conf['target_latency'])) * 660), 64))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + str(int(query_count)+40) + "\n"
            #user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
            if short_ranging:
                ranging_user_conf += ml_model_name + "." + scenario + ".max_query_count = " + str(int(query_count)+40) + "\n"
        elif scenario == "Offline":
            query_count = int(float(conf['target_qps']) * 660)
            query_count = str(max(query_count, required_min_queries_offline))

            #user_conf += ml_model_name + "." + scenario + ".max_query_count = " + str(int(query_count)+40) + "\n"
            if short_ranging:
                ranging_query_count = str(int(float(conf['target_qps']) * 300))
                ranging_user_conf += ml_model_name + "." + scenario + ".max_query_count = " + str(ranging_query_count) + "\n"
                ranging_user_conf += ml_model_name + "." + scenario + ".min_query_count = 0 \n"

    if query_count:
        env['CM_MAX_EXAMPLES'] = query_count #needed for squad accuracy checker


    import uuid
    from pathlib import Path
    key = uuid.uuid4().hex
    user_conf_path = os.path.join(script_path, "tmp", key+".conf")
    user_conf_file = Path(user_conf_path)
    user_conf_file.parent.mkdir(exist_ok=True, parents=True)
    user_conf_file.write_text(user_conf)

    if short_ranging:
        ranging_user_conf_path = os.path.join(script_path, "tmp", "ranging_"+key+".conf")
        ranging_user_conf_file = Path(ranging_user_conf_path)
        ranging_user_conf_file.write_text(ranging_user_conf)


    if (env.get('CM_MLPERF_LOADGEN_QUERY_COUNT','') == '')  and query_count and ((mode != "accuracy") or (env['CM_MLPERF_RUN_STYLE'] != "valid")):
        env['CM_MLPERF_LOADGEN_QUERY_COUNT'] = query_count

    if not run_exists or rerun:

        print("Output Dir: '" + OUTPUT_DIR + "'")
        print(user_conf)
        if env.get('CM_MLPERF_POWER','') == "yes" and os.path.exists(env.get('CM_MLPERF_POWER_LOG_DIR', '')):
            shutil.rmtree(env['CM_MLPERF_POWER_LOG_DIR'])
    else:
        if not env.get('CM_MLPERF_COMPLIANCE_RUN_POSTPONED', False):
            print("Run files exist, skipping run...\n")
        env['CM_MLPERF_SKIP_RUN'] = "yes"

    if not run_exists or rerun or not measure_files_exist(OUTPUT_DIR, \
                    required_files[4]) or env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes" or env.get("CM_REGENERATE_MEASURE_FILES", False):

        env['CM_MLPERF_TESTING_USER_CONF'] = os.path.join(os.path.dirname(user_conf_path), key+".conf")#  user_conf_path
        env['CM_MLPERF_RANGING_USER_CONF'] = os.path.join(os.path.dirname(user_conf_path), "ranging_"+key+".conf")#  ranging_user_conf_path for a shorter run

        if short_ranging:
            env['CM_MLPERF_USER_CONF'] = "\${CM_MLPERF_USER_CONF}"
        else:
            env['CM_MLPERF_USER_CONF'] = os.path.join(os.path.dirname(user_conf_path), key+".conf")#  user_conf_path
    else:
        print(f"Measure files exist at {OUTPUT_DIR}. Skipping regeneration...\n")
        env['CM_MLPERF_USER_CONF'] = ''

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    return {'return':0}

def run_files_exist(mode, OUTPUT_DIR, run_files, env):
    import submission_checker as checker
    from log_parser import MLPerfLog

    is_valid = True

    file_loc = {"accuracy": 0, "performance": 1, "power": 2, "performance_power": 3, "measure": 4, "compliance": 1}

    required_files = run_files[file_loc[mode]]
    if mode == "performance_power":
        for file_ in run_files[2]:
            file_path = os.path.join(os.path.dirname(OUTPUT_DIR), "power", file_)
            if (not os.path.exists(file_path) or os.stat(file_path).st_size == 0):
                return False
        required_files += run_files[1] #We need performance files too in the run directory

    for file_ in required_files:
        file_path = os.path.join(OUTPUT_DIR, file_)
        if (not os.path.exists(file_path) or os.stat(file_path).st_size == 0)  and file_ != "accuracy.txt":
            return False

        if file_ ==  "mlperf_log_detail.txt" and "performance" in mode:
            mlperf_log = MLPerfLog(file_path)
            if (
                "result_validity" not in mlperf_log.get_keys()
                or mlperf_log["result_validity"] != "VALID"
            ):
                return False

    if mode == "compliance":
        #If a performance run followed the last compliance run, compliance check needs to be redone
        RESULT_DIR = os.path.split(OUTPUT_DIR)[0]
        COMPLIANCE_DIR = OUTPUT_DIR
        OUTPUT_DIR = os.path.dirname(COMPLIANCE_DIR)

        #If reference test result is invalid, don't do compliance run
        file_path = os.path.join(RESULT_DIR, "performance", "run_1", "mlperf_log_detail.txt")
        mlperf_log = MLPerfLog(file_path)
        if (
            "result_validity" not in mlperf_log.get_keys()
            or mlperf_log["result_validity"] != "VALID"
        ):
            env['CM_MLPERF_COMPLIANCE_RUN_POSTPONED'] = True
            return True

        test = env['CM_MLPERF_LOADGEN_COMPLIANCE_TEST']

        SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", test, "run_verification.py")
        cmd = env['CM_PYTHON_BIN'] + " " + SCRIPT_PATH + " -r " + RESULT_DIR + " -c " + COMPLIANCE_DIR + " -o "+ OUTPUT_DIR
        print(cmd)
        os.system(cmd)

        is_valid = checker.check_compliance_perf_dir(COMPLIANCE_DIR)

        if not is_valid and 'Stream' in env['CM_MLPERF_LOADGEN_SCENARIO']:
            env['CM_MLPERF_USE_MAX_DURATION'] = 'no' # We have the determined latency, compliance test failed, so lets not use max duration
            env['CM_MLPERF_INFERENCE_MIN_DURATION'] = '990000' # Try a longer run

        return is_valid

    if "power" in mode and env.get('CM_MLPERF_SKIP_POWER_CHECKS', 'no').lower() not in [ "yes", "true", "on" ]:
        from power.power_checker import check as check_power_more
        try:
            is_valid = check_power_more(os.path.dirname(OUTPUT_DIR)) == 0
        except:
            is_valid = False
        return is_valid

    return is_valid

def measure_files_exist(OUTPUT_DIR, run_files):
    for file in run_files:
        file_path = os.path.join(OUTPUT_DIR, file)
        if not os.path.exists(file_path):
            return False
    return True

def get_checker_files():
    import submission_checker as checker

    REQUIRED_ACC_FILES = checker.REQUIRED_ACC_FILES
    REQUIRED_PERF_FILES = checker.REQUIRED_PERF_FILES
    REQUIRED_POWER_FILES = checker.REQUIRED_POWER_FILES
    REQUIRED_PERF_POWER_FILES = checker.REQUIRED_PERF_POWER_FILES
    REQUIRED_MEASURE_FILES = checker.REQUIRED_MEASURE_FILES
    return REQUIRED_ACC_FILES, REQUIRED_PERF_FILES, REQUIRED_POWER_FILES, REQUIRED_PERF_POWER_FILES, REQUIRED_MEASURE_FILES

def get_required_min_queries_offline(model, version):

    import submission_checker as checker

    version_split = version.split(".")
    if int(version[0]) < 4:
        return 24756

    REQUIRED_MIN_QUERIES = checker.OFFLINE_MIN_SPQ_SINCE_V4
    mlperf_model = model
    mlperf_model = mlperf_model.replace("resnet50", "resnet")

    return REQUIRED_MIN_QUERIES[mlperf_model]
