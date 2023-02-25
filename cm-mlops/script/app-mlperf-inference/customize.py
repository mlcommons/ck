from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm

def preprocess(i):

    env = i['env']

    if env.get('CM_MLPERF_SUBMISSION_GENERATION_STYLE', '') == "short":
        if env.get('CM_MODEL', '') == "resnet50":
            env['CM_TEST_QUERY_COUNT'] = "500" #so that accuracy script doesn't complain

    return {'return':0}

def postprocess(i):

    env = i['env']
    inp = i['input']
    state = i['state']

    if env.get('CM_MLPERF_USER_CONF', '') == '':
        return {'return': 0}
    output_dir = env['CM_MLPERF_OUTPUT_DIR']
    mode = env['CM_MLPERF_LOADGEN_MODE']

    #in power mode copy the log files from tmp_power directory
    if env.get('CM_MLPERF_POWER', '') == "yes" and mode == "performance":
        mlperf_power_logs_dir = os.path.join(env['CM_MLPERF_OUTPUT_DIR'], "..", "power")
        mlperf_ranging_logs_dir = os.path.join(env['CM_MLPERF_OUTPUT_DIR'], "..", "ranging")

        if os.path.exists(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "power")):
            if os.path.exists(mlperf_power_logs_dir):
                shutil.rmtree(mlperf_power_logs_dir)
            shutil.copytree(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "power"), mlperf_power_logs_dir)

        if os.path.exists(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "ranging")):
            if os.path.exists(mlperf_ranging_logs_dir):
                shutil.rmtree(mlperf_ranging_logs_dir)
            shutil.copytree(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "ranging"), mlperf_ranging_logs_dir)

        if os.path.exists(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "run_1", "spl.txt")):
            shutil.copyfile(os.path.join(env['CM_MLPERF_POWER_LOG_DIR'], "run_1", "spl.txt"), os.path.join(env['CM_MLPERF_OUTPUT_DIR'], "spl.txt"))

    accuracy_result_dir = ''
    model = env['CM_MODEL']
    model_full_name = env.get('CM_ML_MODEL_FULL_NAME', model)

    if model == "resnet50":
        accuracy_filename = "accuracy-imagenet.py"
        dataset_args = " --imagenet-val-file " + \
        os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")

    elif model == "retinanet":
        accuracy_filename = "accuracy-openimages.py"
        dataset_args = " --openimages-dir " + env['CM_DATASET_PATH']

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']

    if env.get("CM_MLPERF_FIND_PERFORMANCE", False) and mode == "performance" and scenario != "Server":
        os.chdir(output_dir)
        if not os.path.exists("mlperf_log_summary.txt"):
            return {'return': 0}

        if scenario in [ "Offline", "Server" ]:
            metric = "target_qps"
        elif scenario.endswith("Stream"):
            metric = "target_latency"
        else:
            return {'return': 1, 'error': 'Unsupported scenario: {}'.format(scenario)}

        import re
        import yaml
        pattern = {}
        pattern["Offline"] = "Samples per second: (.*)\n"
        pattern["SingleStream"] = "Mean latency \(ns\)\s*:(.*)"
        pattern["MultiStream"] = "Mean latency \(ns\)\s*:(.*)"
        print("\n")
        with open("mlperf_log_summary.txt", "r") as fp:
            summary = fp.read()
        print(summary)
        result = re.findall(pattern[scenario], summary)

        if not result:
            return {'return': 1, 'error': f'No {metric} found in performance summary. Pattern checked "{pattern[metric]}"'}

        value = result[0].strip()
        if "\(ns\)" in pattern[scenario]:
            value = str(float(value)/1000000) #convert to milliseconds

        sut_name = state['CM_SUT_CONFIG_NAME']
        sut_config = state['CM_SUT_CONFIG'][sut_name]
        sut_config_path = state['CM_SUT_CONFIG_PATH'][sut_name]
        sut_config[model_full_name][scenario][metric] = value

        print(f"SUT: {sut_name}, model: {model_full_name}, scenario: {scenario}, {metric} updated as {value}")
        print(f"New config stored in {sut_config_path}")
        with open(sut_config_path, "w") as f:
            yaml.dump(sut_config, f)


    elif mode in [ "performance", "accuracy" ]:
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

        if env.get('CM_MLPERF_README', '') == "yes":
            readme_body += "\n## Dependent CM scripts \n"

            script_tags = inp['tags']
            script_adr = inp.get('adr', {})

            cm_input = {'action': 'run',
                    'automation': 'script',
                    'tags': script_tags,
                    'adr': script_adr,
                    'print_deps': True,
                    'env': env,
                    'quiet': True,
                    'silent': True,
                    'fake_run': True
                    }
            r = cm.access(cm_input)
            if r['return'] > 0:
                return r

            print_deps = r['new_state']['print_deps']
            count = 1
            for dep in print_deps:
                readme_body += "\n\n" + str(count) +".  `" +dep+ "`\n"
                count = count+1

            if state.get('mlperf-inference-implementation') and state['mlperf-inference-implementation'].get('print_deps'):

                readme_body += "\n## Dependent CM scripts for the MLPerf Inference Implementation\n"

                print_deps = state['mlperf-inference-implementation']['print_deps']
                count = 1
                for dep in print_deps:
                    readme_body += "\n\n" + str(count) +". `" +dep+"`\n"
                    count = count+1

            readme = readme_init + readme_body
            with open ("README.md", "w") as fp:
                fp.write(readme)

    elif mode == "compliance":

        test = env.get("CM_MLPERF_LOADGEN_COMPLIANCE_TEST", "TEST01")

        RESULT_DIR = os.path.split(output_dir)[0]
        COMPLIANCE_DIR = output_dir
        '''split = os.path.split(RESULT_DIR)
        split = os.path.split(split[0])
        model = split[1]
        split = os.path.split(split[0])
        sut = split[1]
        split = os.path.split(split[0])
        OUTPUT_DIR = os.path.join(split[0], "compliance", sut, model, scenario)
        '''
        OUTPUT_DIR = os.path.dirname(COMPLIANCE_DIR)

        SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", test, "run_verification.py")
        cmd = env['CM_PYTHON_BIN'] + " " + SCRIPT_PATH + " -r " + RESULT_DIR + " -c " + COMPLIANCE_DIR + " -o "+ OUTPUT_DIR
        print(cmd)
        os.system(cmd)

        if test == "TEST01":
            SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", test,
                    "create_accuracy_baseline.sh")
            ACCURACY_DIR = os.path.join(RESULT_DIR, "accuracy")
            if not os.path.exists(ACCURACY_DIR):
                print("Accuracy run not yet completed")
                return {'return':1, 'error': 'TEST01 needs accuracy run to be completed first'}

            cmd = "bash " + SCRIPT_PATH + " " + os.path.join(ACCURACY_DIR, "mlperf_log_accuracy.json") + " " + \
                    os.path.join(COMPLIANCE_DIR, "mlperf_log_accuracy.json")
            print(cmd)
            result  = subprocess.run(cmd, shell=True)

            CMD = "cat verify_accuracy.txt | grep 'TEST PASS'"
            try:
                result  = subprocess.check_output(CMD, shell=True).decode("utf-8")
            except subprocess.CalledProcessError as e:
            #if not result: #Normal test failed, trying the check with non-determinism

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
        print(test)

    if accuracy_result_dir != '':
        env['CM_MLPERF_ACCURACY_RESULTS_DIR'] = accuracy_result_dir

    return {'return':0}
