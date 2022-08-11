from cmind import utils
import os
import json
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

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

    if 'CM_ALL_SCENARIOS' in env:
        system_meta = state['CM_SUT_META']
        env['CM_LOADGEN_SCENARIOS'] = get_valid_scenarios(env['CM_MODEL'], system_meta['system_type'], env['CM_MLC_LAST_RELEASE'], env['CM_MLC_INFERENCE_SOURCE'])
    else:
        env['CM_LOADGEN_SCENARIOS'] = [ env['CM_LOADGEN_SCENARIO'] ]

    if 'CM_ALL_MODES' in env:
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

    print("Using MLCommons Inference source from " + env['CM_MLC_INFERENCE_SOURCE'])

    if 'CM_MLC_MLPERF_CONF' not in env:
        env['CM_MLC_MLPERF_CONF'] = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "mlperf.conf")


    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  " --mlperf_conf " + env['CM_MLC_MLPERF_CONF']

    env['DATA_DIR'] = env['CM_DATASET_PATH']
    env['MODEL_DIR'] = env['CM_ML_MODEL_PATH']

    env['RUN_DIR'] = env['CM_MLC_INFERENCE_SOURCE'] + "/vision/classification_and_detection"
    RUN_CMDS = []
    state['RUN'] = []

    for scenario in env['CM_LOADGEN_SCENARIOS']:
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
            query_count = "10"
            user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
            user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
        elif env['CM_RUN_STYLE'] == "fast":
            if scenario == "Server":
                target_qps = conf['target_qps']
                query_count = str((660/fast_factor)/(float(target_qps)))
                user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
                user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
        else:
            if scenario == "MultiStream":
                query_count = str(int((8000 / float(conf['target_latency'])) * 660))
                user_conf += env['CM_MODEL'] + "." + scenario + ".max_query_count = " + query_count + "\n"
                user_conf += env['CM_MODEL'] + "." + scenario + ".min_query_count = " + query_count + "\n"
        print(user_conf)
        import uuid
        key = uuid.uuid4().hex
        user_conf_path = os.path.join(script_path, "tmp", key+".conf")
        from pathlib import Path
        user_conf_file = Path(user_conf_path)
        user_conf_file.parent.mkdir(exist_ok=True, parents=True)
        user_conf_file.write_text(user_conf)
        scenario_extra_options +=  " --user_conf " + user_conf_path

        for mode in env['CM_LOADGEN_MODES']:
            mode_extra_options = ""
            if mode == "accuracy":
                mode_extra_options += " --accuracy"
            OUTPUT_DIR =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'],
                        env['CM_BACKEND'] + "-" + env['CM_DEVICE'], env['CM_MODEL'], scenario.lower(),
                        mode)
            print("Output Dir:" + OUTPUT_DIR)

            cmd =  "cd "+ env['RUN_DIR'] + " && OUTPUT_DIR=" + OUTPUT_DIR + " ./run_local.sh " + env['CM_BACKEND'] + ' ' + env['CM_MODEL'] + ' ' + env['CM_DEVICE'] + " --scenario " + scenario + " " + env['CM_LOADGEN_EXTRA_OPTIONS'] + scenario_extra_options + mode_extra_options 
            RUN_CMDS.append(cmd)
            state['RUN'] += [ { "CM_MLC_RUN_CMD": cmd, "OUTPUT_DIR": OUTPUT_DIR, "CM_MLC_USER_CONF" : user_conf_path
                } ]

    env['CM_MLC_RUN_CMDS'] = "??".join(RUN_CMDS)
    return {'return':0}

def get_valid_scenarios(model, category, mlc_version, mlc_path):
    import sys
    submission_checker_dir = os.path.join(mlc_path, "tools", "submission")
    submission_checker = os.path.join(submission_checker_dir, "submission-checker.py")
    sys.path.append(".")
    sys.path.append(submission_checker_dir)
    shutil.copy(submission_checker, "checker.py")
    import checker
    config = checker.MODEL_CONFIG
    internal_model_name = config[mlc_version]["model_mapping"][model]
    valid_scenarios = config[mlc_version]["required-scenarios-"+category][internal_model_name]
    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))
    return valid_scenarios


def postprocess(i):
    env = i['env']
    state = i['state']
    #print(state['RUN']) 
    for run in state['RUN']:
        measurements = {}
        measurements['retraining'] = env.get('CM_MODEL_RETRAINING','')
        measurements['starting_weights_filename'] = env.get('CM_STARTING_WEIGHTS_FILENAME', 'none')
        measurements['input_data_types'] = env.get('CM_MODEL_INPUT_DATA_TYPES', 'fp32')
        measurements['weight_data_types'] = env.get('CM_MODEL_WEIGHT_DATA_TYPES', 'fp32')
        measurements['weight_transformations'] = env.get('CM_MODEL_WEIGHT_TRANSFORMATIONS', 'none')
        os.chdir(run['OUTPUT_DIR'])
        with open ("measurements.json", "w") as fp:
            json.dump(measurements, fp, indent=2)
        if os.path.exists(env['CM_MLC_MLPERF_CONF']):
            shutil.copy(env['CM_MLC_MLPERF_CONF'], 'mlperf.conf')
        if os.path.exists(run['CM_MLC_USER_CONF']):
            shutil.copy(run['CM_MLC_USER_CONF'], 'user.conf')
        env['CM_MLC_RESULTS_DIR'] = run['OUTPUT_DIR']
        readme_init = ""
        readme_body = "##\n```\n" + run['CM_MLC_RUN_CMD'] + "\n```"
        readme = readme_init + readme_body
        with open ("README.md", "w") as fp:
            fp.write(readme)


    return {'return':0}
