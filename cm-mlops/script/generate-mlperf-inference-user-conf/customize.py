from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm

def preprocess(i):


    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    rerun = True if env.get("CM_RERUN","")!='' else False

    env['CM_MLPERF_SKIP_RUN'] = "no"
    required_files = []
    required_files = get_checker_files(env['CM_MLPERF_INFERENCE_SOURCE'])

    if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
        env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if 'CM_MLPERF_LOADGEN_MODE' not in env:
        env['CM_MLPERF_LOADGEN_MODE'] = "accuracy"


    if 'OUTPUT_BASE_DIR' not in env:
        env['OUTPUT_BASE_DIR'] = os.getcwd()

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
    if env['CM_MODEL'] in ["rnnt", "bert-99", "bert-99.9", "dlrm-99", "dlrm-99.9", "3d-unet-99", "3d-unet-99.9"]:
        test_list.remove("TEST04")

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    state['RUN'][scenario] = {}

    if env['CM_MODEL'] not in i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']]:
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']] = {}
        i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][scenario] = {}


    conf = i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][scenario]

    mode = env['CM_MLPERF_LOADGEN_MODE']

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
            if env.get("CM_MLPERF_FIND_PERFORMANCE", "no") == "yes":
                if metric == "target_qps":
                    print("In find performance mode: using 1 as target_qps")
                    conf[metric] = 1
                if metric == "target_latency":
                    print("In find performance mode: using 1000 as target_latency")
                    conf[metric] = 1000
            else:
                return {'return': 1, 'error': f"Config details missing for SUT:{env['CM_SUT_NAME']}, Model:{env['CM_MODEL']}, Scenario: {scenario}. Please input {metric} value"}

    #Pass the modified performance metrics to the implementation
    if env.get("CM_MLPERF_FIND_PERFORMANCE", "no") == "yes":
        if metric == "target_latency" and env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY', '') == '':
            env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = conf[metric]
        elif metric == "target_qps" and env.get('CM_MLPERF_LOADGEN_TARGET_QPS', '') == '':
            env['CM_MLPERF_LOADGEN_TARGET_QPS'] = conf[metric]


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

    elif env['CM_MLPERF_RUN_STYLE'] == "fast":
        if scenario == "Server":
            target_qps = conf['target_qps']
            query_count = str((660/fast_factor)/(float(target_qps)))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_duration = 0" + "\n"

    else:
        if scenario == "MultiStream":
            query_count = str(int((8000 / float(conf['target_latency'])) * 660))
            user_conf += ml_model_name + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += ml_model_name + "." + scenario + ".min_query_count = " + query_count + "\n"

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

    env['CM_MLPERF_RESULTS_DIR'] = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])

    sut_name = env.get('CM_SUT_NAME', env['CM_MLPERF_BACKEND'] + "-" + env['CM_MLPERF_DEVICE'])
    OUTPUT_DIR =  os.path.join(env['CM_MLPERF_RESULTS_DIR'], sut_name, \
            env['CM_MODEL'], scenario.lower(), mode)

    if 'CM_MLPERF_POWER' in env:
        env['CM_MLPERF_POWER_LOG_DIR'] = os.path.join(OUTPUT_DIR, "tmp_power")

    if mode == "accuracy":
        pass
    elif mode == "performance":
        OUTPUT_DIR = os.path.join(OUTPUT_DIR, "run_1")
    elif mode == "compliance":
        test = env.get("CM_MLPERF_LOADGEN_COMPLIANCE_TEST", "TEST01")
        OUTPUT_DIR =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'], sut_name, env['CM_MODEL'], scenario.lower(), test)
        if test == "TEST01":
            audit_path = os.path.join(test, env['CM_MODEL'])
        else:
            audit_path = test

        audit_full_path = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", audit_path, "audit.config")
        env['CM_MLPERF_INFERENCE_AUDIT_PATH'] = audit_full_path

    env['CM_MLPERF_OUTPUT_DIR'] = OUTPUT_DIR
    env['CM_MLPERF_LOADGEN_LOGS_DIR'] = OUTPUT_DIR
    log_mode = mode
    if 'CM_MLPERF_POWER' in env and mode == "performance":
        log_mode = "performance_power"
    
    if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun:
        print("Output Dir: '" + OUTPUT_DIR + "'")
        print(user_conf)
        if 'CM_MLPERF_POWER' in env and os.path.exists(env['CM_MLPERF_POWER_LOG_DIR']):
            shutil.rmtree(env['CM_MLPERF_POWER_LOG_DIR'])
    else:
        print("Run files exist, skipping run...\n")
        env['CM_MLPERF_SKIP_RUN'] = "yes"

    if not run_files_exist(mode, OUTPUT_DIR, required_files) or rerun or not measure_files_exist(OUTPUT_DIR, \
                    required_files[4]) or env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes" or env.get("CM_REGENERATE_MEASURE_FILES", False):
        env['CM_MLPERF_USER_CONF'] = user_conf_path
    else:
        print("Measure files exist, skipping regeneration...\n")
        env['CM_MLPERF_USER_CONF'] = ''

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    return {'return':0}

def run_files_exist(mode, OUTPUT_DIR, run_files):
    file_loc = {"accuracy": 0, "performance": 1, "power": 2, "performance_power": 3, "measure": 4, "compliance": 1}
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
