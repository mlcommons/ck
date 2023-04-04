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
        accuracy_filepath = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                        accuracy_filename)
        dataset_args = " --imagenet-val-file " + \
        os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")
        accuracy_log_file_option_name = " --mlperf-accuracy-file "
        datatype_option = " --dtype "+env['CM_IMAGENET_ACCURACY_DTYPE']

    elif model == "retinanet":
        accuracy_filename = "accuracy-openimages.py"
        accuracy_filepath = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                        accuracy_filename)
        dataset_args = " --openimages-dir " + env['CM_DATASET_PATH']
        accuracy_log_file_option_name = " --mlperf-accuracy-file "
        datatype_option = ""

    elif 'bert' in model:
        accuracy_filename = "accuracy-squad.py"
        accuracy_filepath = os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'], accuracy_filename)
        dataset_args = " --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + "' --vocab_file '" + env['CM_DATASET_SQUAD_VOCAB_PATH'] + "' --out_file predictions.json "
        accuracy_log_file_option_name = " --log_file "
        datatype_option = " --output_dtype "+env['CM_SQUAD_ACCURACY_DTYPE']

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']

    if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes" and mode == "performance" and scenario != "Server":
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
        measurements['starting_weights_filename'] = env.get('CM_ML_MODEL_STARTING_WEIGHTS_FILENAME', env.get('CM_ML_MODEL_FILE', ''))
        measurements['retraining'] = env.get('CM_ML_MODEL_RETRAINING','no')
        measurements['input_data_types'] = env.get('CM_ML_MODEL_INPUTS_DATA_TYPE', 'fp32')
        measurements['weight_data_types'] = env.get('CM_ML_MODEL_WEIGHTS_DATA_TYPE', 'fp32')
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
        OUTPUT_DIR = os.path.dirname(COMPLIANCE_DIR)

        SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", test, "run_verification.py")
        cmd = env['CM_PYTHON_BIN'] + " " + SCRIPT_PATH + " -r " + RESULT_DIR + " -c " + COMPLIANCE_DIR + " -o "+ OUTPUT_DIR
        print(cmd)
        os.system(cmd)

        if test == "TEST01":

            run_script_input = i['run_script_input']
            automation = i['automation']

            SCRIPT_PATH = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "compliance", "nvidia", test,
                    "create_accuracy_baseline.sh")
            TEST01_DIR = os.path.join(OUTPUT_DIR, "TEST01")
            OUTPUT_DIR = os.path.join(OUTPUT_DIR, "TEST01", "accuracy")
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)

            ACCURACY_DIR = os.path.join(RESULT_DIR, "accuracy")
            if not os.path.exists(ACCURACY_DIR):
                print("Accuracy run not yet completed")
                return {'return':1, 'error': 'TEST01 needs accuracy run to be completed first'}

            cmd = "cd " + TEST01_DIR + " &&  bash " + SCRIPT_PATH + " " + os.path.join(ACCURACY_DIR, "mlperf_log_accuracy.json") + " " + \
                    os.path.join(COMPLIANCE_DIR, "mlperf_log_accuracy.json")
            env['CMD'] = cmd
            r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'verify_accuracy'})
            if r['return']>0:
                return r

            verify_accuracy_file = os.path.join(TEST01_DIR, "verify_accuracy.txt")
            with open(verify_accuracy_file, 'r') as file:
                data = file.read().replace('\n', '\t')

            if 'TEST PASS' not in data:
                print("\nDeterministic TEST01 failed... Trying with non-determinism.\n")
            # #Normal test failed, trying the check with non-determinism

                CMD = "cd "+ ACCURACY_DIR+" && "+  env['CM_PYTHON_BIN'] + ' ' + accuracy_filepath + accuracy_log_file_option_name + \
                        os.path.join(TEST01_DIR, "mlperf_log_accuracy_baseline.json") + dataset_args + datatype_option + " > " + \
                        os.path.join(OUTPUT_DIR, "baseline_accuracy.txt")

                env['CMD'] = CMD
                r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'verify_accuracy'})
                if r['return']>0: return r

                CMD = "cd " + ACCURACY_DIR + " &&  "+env['CM_PYTHON_BIN'] + ' ' + accuracy_filepath + accuracy_log_file_option_name + \
                        os.path.join(TEST01_DIR, "mlperf_log_accuracy.json") + dataset_args + datatype_option + " > " + \
                        os.path.join(OUTPUT_DIR, "compliance_accuracy.txt")

                env['CMD'] = CMD
                r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'verify_accuracy'})
                if r['return']>0: return r

    else:
        print(test)

    if accuracy_result_dir != '':
        env['CM_MLPERF_ACCURACY_RESULTS_DIR'] = accuracy_result_dir

    return {'return':0}
