#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils

import os
import json
import shutil
import subprocess
import copy
import cmind as cm
import platform
import sys
import mlperf_utils
import re
from datetime import datetime, timezone


def preprocess(i):

    env = i['env']
    state = i['state']

    if env.get('CM_MLPERF_IMPLEMENTATION', '') == 'nvidia':
        if env.get('CM_NVIDIA_GPU_NAME', '') in [
                "rtx_4090", "a100", "t4", "l4", "orin", "custom"]:
            env['CM_NVIDIA_HARNESS_GPU_VARIATION'] = "_" + \
                env['CM_NVIDIA_GPU_NAME']
            env['CM_NVIDIA_GPU_MEMORY'] = ''
        else:
            gpu_memory = i['state'].get(
                'cm_cuda_device_prop', '').get('Global memory')
            gpu_memory_size = str(
                int((float(gpu_memory) / (1024 * 1024 * 1024) + 7) / 8) * 8)
            env['CM_NVIDIA_GPU_MEMORY'] = gpu_memory_size
            env['CM_NVIDIA_HARNESS_GPU_VARIATION'] = ''

    if 'cmd' in i['input']:
        state['mlperf_inference_run_cmd'] = "cm run script " + \
            " ".join(i['input']['cmd'])

    state['mlperf-inference-implementation'] = {}

    run_state = i['run_script_input']['run_state']
    state['mlperf-inference-implementation']['script_id'] = run_state['script_id'] + \
        ":" + ",".join(run_state['script_variation_tags'])

    if env.get('CM_VLLM_SERVER_MODEL_NAME', '') != '' and env.get(
            'CM_ML_MODEL_FULL_NAME', '') == '':
        env['CM_ML_MODEL_FULL_NAME'] = env['CM_VLLM_SERVER_MODEL_NAME'].replace(
            "/", "_")

    return {'return': 0}


def postprocess(i):

    os_info = i['os_info']

    xsep = '^' if os_info['platform'] == 'windows' else '\\'

    env = i['env']
    inp = i['input']
    env['CMD'] = ''
    state = i['state']

    # if env.get('CM_MLPERF_USER_CONF', '') == '':
    #    return {'return': 0}

    output_dir = env['CM_MLPERF_OUTPUT_DIR']

    result_sut_folder_path = env['CM_MLPERF_INFERENCE_RESULTS_SUT_PATH']

    mode = env['CM_MLPERF_LOADGEN_MODE']

    if not os.path.exists(output_dir) or not os.path.exists(
            os.path.join(output_dir, "mlperf_log_summary.txt")):
        # No output, fake_run?
        return {'return': 0}

    # in power mode copy the log files from tmp_power directory
    if env.get('CM_MLPERF_POWER', '') == "yes" and mode == "performance":
        mlperf_power_logs_dir = os.path.join(
            env['CM_MLPERF_OUTPUT_DIR'], "..", "power")
        mlperf_ranging_logs_dir = os.path.join(
            env['CM_MLPERF_OUTPUT_DIR'], "..", "ranging")

        if os.path.exists(os.path.join(
                env['CM_MLPERF_POWER_LOG_DIR'], "power")):
            if os.path.exists(mlperf_power_logs_dir):
                shutil.rmtree(mlperf_power_logs_dir)
            shutil.copytree(
                os.path.join(
                    env['CM_MLPERF_POWER_LOG_DIR'],
                    "power"),
                mlperf_power_logs_dir)

        if os.path.exists(os.path.join(
                env['CM_MLPERF_POWER_LOG_DIR'], "ranging")):
            if os.path.exists(mlperf_ranging_logs_dir):
                shutil.rmtree(mlperf_ranging_logs_dir)
            shutil.copytree(
                os.path.join(
                    env['CM_MLPERF_POWER_LOG_DIR'],
                    "ranging"),
                mlperf_ranging_logs_dir)

        if os.path.exists(os.path.join(
                env['CM_MLPERF_POWER_LOG_DIR'], "run_1", "spl.txt")):
            shutil.copyfile(
                os.path.join(
                    env['CM_MLPERF_POWER_LOG_DIR'],
                    "run_1",
                    "spl.txt"),
                os.path.join(
                    env['CM_MLPERF_OUTPUT_DIR'],
                    "spl.txt"))

    model = env['CM_MODEL']
    model_full_name = env.get('CM_ML_MODEL_FULL_NAME', model)

    if mode == "accuracy" or mode == "compliance" and env[
            'CM_MLPERF_LOADGEN_COMPLIANCE_TEST'] == "TEST01":
        if model == "resnet50":
            accuracy_filename = "accuracy-imagenet.py"
            accuracy_filepath = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools",
                                             accuracy_filename)
            dataset_args = " --imagenet-val-file " + \
                os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt")
            accuracy_log_file_option_name = " --mlperf-accuracy-file "
            datatype_option = " --dtype " + env['CM_IMAGENET_ACCURACY_DTYPE']

        elif model == "retinanet":
            accuracy_filename = "accuracy-openimages.py"
            accuracy_filepath = os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools",
                                             accuracy_filename)
            dataset_args = " --openimages-dir " + \
                os.getcwd()  # just to make the script happy
            accuracy_log_file_option_name = " --mlperf-accuracy-file "
            datatype_option = ""

        elif 'bert' in model:
            accuracy_filename = "accuracy-squad.py"
            accuracy_filepath = os.path.join(
                env['CM_MLPERF_INFERENCE_BERT_PATH'], accuracy_filename)
            dataset_args = " --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + "' --vocab_file '" + \
                env['CM_DATASET_SQUAD_VOCAB_PATH'] + \
                "' --out_file predictions.json "
            accuracy_log_file_option_name = " --log_file "
            datatype_option = " --output_dtype " + \
                env['CM_SQUAD_ACCURACY_DTYPE']

        elif 'stable-diffusion-xl' in model:
            pass  # No compliance check for now
        elif 'gpt' in model:
            pass  # No compliance check for now
        elif 'llama2-70b' in model:
            pass  # No compliance check for now
        elif 'mixtral-8x7b' in model:
            pass  # No compliance check for now
        else:
            pass  # Not giving an error now. But accuracy paths need to be done for other benchmarks which may need the non-determinism test
            # return {'return': 1, 'error': f'Accuracy paths not done for model
            # {model}'}
    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']

    if not state.get('cm-mlperf-inference-results'):
        state['cm-mlperf-inference-results'] = {}
    if not state.get('cm-mlperf-inference-results-last'):
        state['cm-mlperf-inference-results-last'] = {}
    if not state['cm-mlperf-inference-results'].get(
            state['CM_SUT_CONFIG_NAME']):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']] = {}
    if not state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                ].get(model):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']][model] = {}
    if not state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                ][model].get(scenario):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                             ][model][scenario] = {}

    # if env.get("CM_MLPERF_FIND_PERFORMANCE_MODE", '') == "yes" and mode ==
    # "performance" and scenario != "Server":
    if mode == "performance" and scenario != "Server":
        os.chdir(output_dir)
        if not os.path.exists("mlperf_log_summary.txt"):
            return {'return': 0}

        if scenario in ["Offline", "Server"]:
            metric = "target_qps"
        elif scenario.endswith("Stream"):
            metric = "target_latency"
        else:
            return {'return': 1,
                    'error': 'Unsupported scenario: {}'.format(scenario)}

        import re
        import yaml
        pattern = {}
        pattern["Offline"] = "Samples per second: (.*)\n"
        pattern["SingleStream"] = "Mean latency \\(ns\\)\\s*:(.*)"
        pattern["MultiStream"] = "Mean latency \\(ns\\)\\s*:(.*)"
        print("\n")
        with open("mlperf_log_summary.txt", "r") as fp:
            summary = fp.read()

        result = re.findall(pattern[scenario], summary)

        if not result:
            return {
                'return': 1, 'error': f'No {metric} found in performance summary. Pattern checked "{pattern[metric]}"'}

        value = result[0].strip()
        if "\\(ns\\)" in pattern[scenario]:
            value = str(float(value) / 1000000)  # convert to milliseconds

        sut_name = state['CM_SUT_CONFIG_NAME']
        sut_config = state['CM_SUT_CONFIG'][sut_name]
        sut_config_path = state['CM_SUT_CONFIG_PATH'][sut_name]
        if scenario not in sut_config[model_full_name]:
            sut_config[model_full_name][scenario] = {}
        sut_config[model_full_name][scenario][metric] = value

        print(
            f"SUT: {sut_name}, model: {model_full_name}, scenario: {scenario}, {metric} updated as {value}")
        print(f"New config stored in {sut_config_path}")
        with open(sut_config_path, "w") as f:
            yaml.dump(sut_config, f)

    if mode in ["performance", "accuracy"]:
        # if measurements file exist read it
        if os.path.exists("measurements.json"):
            with open("measurements.json", "r") as file:
                measurements = json.load(file)  # Load JSON data from the file
        else:
            measurements = {}
        measurements['starting_weights_filename'] = env.get(
            'CM_ML_MODEL_STARTING_WEIGHTS_FILENAME', env.get(
                'CM_ML_MODEL_FILE', measurements.get(
                    'starting_weights_filename', '')))
        measurements['retraining'] = env.get(
            'CM_ML_MODEL_RETRAINING', measurements.get(
                'retraining', 'no'))
        measurements['input_data_types'] = env.get(
            'CM_ML_MODEL_INPUTS_DATA_TYPE', measurements.get(
                'input_data_types', 'fp32'))
        measurements['weight_data_types'] = env.get(
            'CM_ML_MODEL_WEIGHTS_DATA_TYPE', measurements.get(
                'weight_data_types', 'fp32'))
        measurements['weight_transformations'] = env.get(
            'CM_ML_MODEL_WEIGHT_TRANSFORMATIONS', measurements.get(
                'weight_transformations', 'none'))

        os.chdir(output_dir)

        if not os.path.exists("mlperf_log_summary.txt"):
            return {'return': 0}

        mlperf_log_summary = ''
        if os.path.isfile("mlperf_log_summary.txt"):
            with open("mlperf_log_summary.txt", "r") as fp:
                mlperf_log_summary = fp.read()

        if mlperf_log_summary != '':
            state['app_mlperf_inference_log_summary'] = {}
            for x in mlperf_log_summary.split('\n'):
                y = x.split(': ')
                if len(y) == 2:
                    state['app_mlperf_inference_log_summary'][y[0].strip().lower()
                                                              ] = y[1].strip()

        if env.get("CM_MLPERF_PRINT_SUMMARY", "").lower() not in [
                "no", "0", "false"]:
            print("\n")
            print(mlperf_log_summary)

        with open("measurements.json", "w") as fp:
            json.dump(measurements, fp, indent=2)

        cm_sut_info = {}
        cm_sut_info['system_name'] = state['CM_SUT_META']['system_name']
        cm_sut_info['implementation'] = env['CM_MLPERF_IMPLEMENTATION']
        cm_sut_info['device'] = env['CM_MLPERF_DEVICE']
        cm_sut_info['framework'] = state['CM_SUT_META']['framework']
        cm_sut_info['run_config'] = env['CM_MLPERF_INFERENCE_SUT_RUN_CONFIG']
        with open(os.path.join(result_sut_folder_path, "cm-sut-info.json"), "w") as fp:
            json.dump(cm_sut_info, fp, indent=2)

        system_meta = state['CM_SUT_META']
        with open("system_meta.json", "w") as fp:
            json.dump(system_meta, fp, indent=2)

        # map the custom model for inference result to the official model
        # if custom model name is not set, the official model name will be
        # mapped to itself
        official_model_name = model
        model_mapping = {model_full_name: official_model_name}
        with open("model_mapping.json", "w") as fp:
            json.dump(model_mapping, fp, indent=2)

        # Add to the state
        state['app_mlperf_inference_measurements'] = copy.deepcopy(
            measurements)

        if os.path.exists(env['CM_MLPERF_CONF']):
            shutil.copy(env['CM_MLPERF_CONF'], 'mlperf.conf')

        if os.path.exists(env['CM_MLPERF_USER_CONF']):
            shutil.copy(env['CM_MLPERF_USER_CONF'], 'user.conf')

        result, valid, power_result = mlperf_utils.get_result_from_log(
            env['CM_MLPERF_LAST_RELEASE'], model, scenario, output_dir, mode, env.get('CM_MLPERF_INFERENCE_SOURCE_VERSION'))
        power = None
        power_efficiency = None
        if power_result:
            power_result_split = power_result.split(",")
            if len(power_result_split) == 2:  # power and power efficiency
                power = power_result_split[0]
                power_efficiency = power_result_split[1]

        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                             ][model][scenario][mode] = result
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                             ][model][scenario][mode + '_valid'] = valid.get(mode, False)

        state['cm-mlperf-inference-results-last'][mode] = result
        state['cm-mlperf-inference-results-last'][mode +
                                                  '_valid'] = valid.get(mode, False)

        if power:
            state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                 ][model][scenario]['power'] = power
            state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                 ][model][scenario]['power_valid'] = valid['power']
            state['cm-mlperf-inference-results-last']['power'] = power
            state['cm-mlperf-inference-results-last']['power_valid'] = valid['power']
        if power_efficiency:
            state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                 ][model][scenario]['power_efficiency'] = power_efficiency
            state['cm-mlperf-inference-results-last']['power_efficiency'] = power_efficiency

        # Record basic host info
        host_info = {
            "os_version": platform.platform(),
            "cpu_version": platform.processor(),
            "python_version": sys.version,
            "cm_version": cm.__version__
        }

        x = ''
        if env.get('CM_HOST_OS_FLAVOR', '') != '':
            x += env['CM_HOST_OS_FLAVOR']
        if env.get('CM_HOST_OS_VERSION', '') != '':
            x += ' ' + env['CM_HOST_OS_VERSION']
        if x != '':
            host_info['os_version_sys'] = x

        if env.get('CM_HOST_SYSTEM_NAME', '') != '':
            host_info['system_name'] = env['CM_HOST_SYSTEM_NAME']

        # Check CM automation repository
        repo_name = 'mlcommons@cm4mlops'
        repo_hash = ''
        r = cm.access({'action': 'find', 'automation': 'repo',
                      'artifact': 'mlcommons@cm4mlops,9e97bb72b0474657'})
        if r['return'] == 0 and len(r['list']) == 1:
            repo_path = r['list'][0].path
            if os.path.isdir(repo_path):
                repo_name = os.path.basename(repo_path)

                # Check dev
                # if repo_name == 'cm4mlops': repo_name = 'mlcommons@cm4mlops'

                r = cm.access({'action': 'system',
                               'automation': 'utils',
                               'path': repo_path,
                               'cmd': 'git rev-parse HEAD'})
                if r['return'] == 0 and r['ret'] == 0:
                    repo_hash = r['stdout']

                    host_info['cm_repo_name'] = repo_name
                    host_info['cm_repo_git_hash'] = repo_hash

        with open("cm-host-info.json", "w") as fp:
            fp.write(json.dumps(host_info, indent=2) + '\n')

        # Prepare README
        if "cmd" in inp:
            cmd = "cm run script \\\n\t" + " \\\n\t".join(inp['cmd'])
            xcmd = "cm run script " + xsep + "\n\t" + \
                (" " + xsep + "\n\t").join(inp['cmd'])
        else:
            cmd = ""
            xcmd = ""

        readme_init = "This experiment is generated using the [MLCommons Collective Mind automation framework (CM)](https://github.com/mlcommons/cm4mlops).\n\n"

        readme_init += "*Check [CM MLPerf docs](https://docs.mlcommons.org/inference) for more details.*\n\n"

        readme_body = "## Host platform\n\n* OS version: {}\n* CPU version: {}\n* Python version: {}\n* MLCommons CM version: {}\n\n".format(platform.platform(),
                                                                                                                                             platform.processor(), sys.version, cm.__version__)

        x = repo_name
        if repo_hash != '':
            x += ' --checkout=' + str(repo_hash)

        readme_body += "## CM Run Command\n\nSee [CM installation guide](https://docs.mlcommons.org/inference/install/).\n\n" + \
            "```bash\npip install -U cmind\n\ncm rm cache -f\n\ncm pull repo {}\n\n{}\n```".format(
                x, xcmd)

        readme_body += "\n*Note that if you want to use the [latest automation recipes](https://docs.mlcommons.org/inference) for MLPerf (CM scripts),\n" + \
                       " you should simply reload {} without checkout and clean CM cache as follows:*\n\n".format(repo_name) + \
                       "```bash\ncm rm repo {}\ncm pull repo {}\ncm rm cache -f\n\n```".format(
                           repo_name, repo_name)

        extra_readme_init = ''
        extra_readme_body = ''
        if env.get('CM_MLPERF_README', '') == "yes":
            extra_readme_body += "\n## Dependent CM scripts\n\n"

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
                extra_readme_body += "\n\n" + str(count) + ".  `" + dep + "`\n"
                count = count + 1

            if state.get(
                    'mlperf-inference-implementation') and state['mlperf-inference-implementation'].get('print_deps'):

                extra_readme_body += "\n## Dependent CM scripts for the MLPerf Inference Implementation\n"

                print_deps = state['mlperf-inference-implementation']['print_deps']
                count = 1
                for dep in print_deps:
                    extra_readme_body += "\n\n" + \
                        str(count) + ". `" + dep + "`\n"
                    count = count + 1

        readme = readme_init + readme_body
        extra_readme = extra_readme_init + extra_readme_body

        with open("README.md", "w") as fp:
            fp.write(readme)
        if extra_readme:
            with open("README-extra.md", "w") as fp:
                fp.write(extra_readme)

    elif mode == "compliance":

        test = env.get("CM_MLPERF_LOADGEN_COMPLIANCE_TEST", "TEST01")

        RESULT_DIR = os.path.split(output_dir)[0]
        COMPLIANCE_DIR = output_dir
        OUTPUT_DIR = os.path.dirname(COMPLIANCE_DIR)

        SCRIPT_PATH = os.path.join(
            env['CM_MLPERF_INFERENCE_SOURCE'],
            "compliance",
            "nvidia",
            test,
            "run_verification.py")
        if test == "TEST06":
            cmd = f"{env['CM_PYTHON_BIN_WITH_PATH']}  {SCRIPT_PATH}  -c  {COMPLIANCE_DIR}  -o  {OUTPUT_DIR} --scenario {scenario} --dtype int32"
        else:
            cmd = f"{env['CM_PYTHON_BIN_WITH_PATH']}  {SCRIPT_PATH}  -r {RESULT_DIR} -c  {COMPLIANCE_DIR}  -o  {OUTPUT_DIR}"

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
                return {
                    'return': 1, 'error': 'TEST01 needs accuracy run to be completed first'}

            cmd = "cd " + TEST01_DIR + " &&  bash " + SCRIPT_PATH + " " + os.path.join(ACCURACY_DIR, "mlperf_log_accuracy.json") + " " + \
                os.path.join(COMPLIANCE_DIR, "mlperf_log_accuracy.json")
            env['CMD'] = cmd
            r = automation.run_native_script(
                {'run_script_input': run_script_input, 'env': env, 'script_name': 'verify_accuracy'})
            if r['return'] > 0:
                return r

            verify_accuracy_file = os.path.join(
                TEST01_DIR, "verify_accuracy.txt")
            with open(verify_accuracy_file, 'r') as file:
                data = file.read().replace('\n', '\t')

            if 'TEST PASS' not in data:
                print("\nDeterministic TEST01 failed... Trying with non-determinism.\n")
            # #Normal test failed, trying the check with non-determinism

                CMD = "cd " + ACCURACY_DIR + " && " + env['CM_PYTHON_BIN_WITH_PATH'] + ' ' + accuracy_filepath + accuracy_log_file_option_name + \
                    os.path.join(TEST01_DIR, "mlperf_log_accuracy_baseline.json") + dataset_args + datatype_option + " > " + \
                    os.path.join(OUTPUT_DIR, "baseline_accuracy.txt")

                env['CMD'] = CMD
                r = automation.run_native_script(
                    {'run_script_input': run_script_input, 'env': env, 'script_name': 'verify_accuracy'})
                if r['return'] > 0:
                    return r

                CMD = "cd " + ACCURACY_DIR + " &&  " + env['CM_PYTHON_BIN_WITH_PATH'] + ' ' + accuracy_filepath + accuracy_log_file_option_name + \
                    os.path.join(TEST01_DIR, "mlperf_log_accuracy.json") + dataset_args + datatype_option + " > " + \
                    os.path.join(OUTPUT_DIR, "compliance_accuracy.txt")

                env['CMD'] = CMD
                r = automation.run_native_script(
                    {'run_script_input': run_script_input, 'env': env, 'script_name': 'verify_accuracy'})
                if r['return'] > 0:
                    return r
        import submission_checker as checker
        is_valid = checker.check_compliance_perf_dir(
            COMPLIANCE_DIR) if test != "TEST06" else True
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                             ][model][scenario][test] = "passed" if is_valid else "failed"

    # portion of the code where the avg utilisation and system informations are extracted
    # NOTE: The section is under development and print statements are added
    # for further debugging
    if env.get('CM_PROFILE_NVIDIA_POWER', '') == "on":
        import pandas as pd
        system_utilisation_info_dump = {}
        logs_dir = output_dir
        # logs_dir = env.get('CM_LOGS_DIR', env['CM_RUN_DIR'])
        sys_utilisation_log = pd.read_csv(
            os.path.join(
                logs_dir,
                'sys_utilisation_info.txt'),
            dtype={
                'cpu_utilisation': float,
                'used_memory_gb': float})
        with open(os.path.join(logs_dir, 'mlperf_log_detail.txt'), 'r') as file:
            log_txt = file.read()
            # patterns for matching the power_begin and power_end in mlperf log
            pattern_begin = r'\"key\"\:\s\"power_begin\"\,\s\"value\"\:\s\"(.*?)\"'
            pattern_end = r'\"key\"\:\s\"power_end\"\,\s\"value\"\:\s\"(.*?)\"'
            # match the patterns with the text present in the log details file
            match_begin = re.findall(pattern_begin, log_txt)[0]
            match_end = re.findall(pattern_end, log_txt)[0]
            power_begin_time = pd.Timestamp(datetime.strptime(
                match_begin, '%m-%d-%Y %H:%M:%S.%f')).replace(tzinfo=timezone.utc)
            power_end_time = pd.Timestamp(datetime.strptime(
                match_end, '%m-%d-%Y %H:%M:%S.%f')).replace(tzinfo=timezone.utc)
        # converts timestamp key value to datetime objects
        sys_utilisation_log['timestamp'] = pd.to_datetime(
            sys_utilisation_log['timestamp'])
        '''
        for i in range(len(sys_utilisation_log['timestamp'])):
            print(f"{sys_utilisation_log['timestamp'][i]} {power_begin_time}")
            print(sys_utilisation_log['timestamp'][i]>=power_begin_time)
        '''
        # print(f"{sys_utilisation_log['timestamp'][0]} {power_begin_time}")
        # print(sys_utilisation_log['timestamp'][0]>=power_begin_time)
        filtered_log = sys_utilisation_log[(sys_utilisation_log['timestamp'] >= power_begin_time) &
                                           (sys_utilisation_log['timestamp'] <= power_end_time)]
        # print(filtered_log)
        # Calculate average of cpu_utilisation and used_memory_gb
        system_utilisation_info_dump["avg_cpu_utilisation"] = filtered_log['cpu_utilisation'].mean(
        )
        system_utilisation_info_dump["avg_used_memory_gb"] = filtered_log['used_memory_gb'].mean(
        )
        print("\nSystem utilisation info for the current run:")
        print(system_utilisation_info_dump)
        print("\n")

    if state.get(
            'mlperf-inference-implementation') and state['mlperf-inference-implementation'].get('version_info'):
        env['CM_MLPERF_RUN_JSON_VERSION_INFO_FILE'] = os.path.join(
            output_dir, "cm-version-info.json")
        env['CM_MLPERF_RUN_DEPS_GRAPH'] = os.path.join(
            output_dir, "cm-deps.png")
        env['CM_MLPERF_RUN_DEPS_MERMAID'] = os.path.join(
            output_dir, "cm-deps.mmd")
        with open(os.path.join(output_dir, "cm-version-info.json"), "w") as f:
            f.write(
                json.dumps(
                    state['mlperf-inference-implementation']['version_info'],
                    indent=2))

    if env.get('CM_DUMP_SYSTEM_INFO', True):
        dump_script_output(
            "detect,os",
            env,
            state,
            'new_env',
            os.path.join(
                output_dir,
                "os_info.json"))
        dump_script_output(
            "detect,cpu",
            env,
            state,
            'new_env',
            os.path.join(
                output_dir,
                "cpu_info.json"))
        env['CM_DUMP_RAW_PIP_FREEZE_FILE_PATH'] = os.path.join(
            env['CM_MLPERF_OUTPUT_DIR'], "pip_freeze.raw")
        dump_script_output(
            "dump,pip,freeze",
            env,
            state,
            'new_state',
            os.path.join(
                output_dir,
                "pip_freeze.json"))

    return {'return': 0}


def dump_script_output(script_tags, env, state, output_key, dump_file):

    cm_input = {'action': 'run',
                'automation': 'script',
                'tags': script_tags,
                'env': env,
                'state': state,
                'quiet': True,
                'silent': True,
                }
    r = cm.access(cm_input)
    if r['return'] > 0:
        return r
    with open(dump_file, "w") as f:
        f.write(json.dumps(r[output_key], indent=2))

    return {'return': 0}
