from cmind import utils
import os
import json
import shutil
import cmind
import sys

def preprocess(i):
    return {'return': 0}

def generate_submission(i):

    # Save current user directory
    cur_dir=os.getcwd()
    env = i['env']
    state = i['state']
    inp=i['input']

    if env.get('CM_MLPERF_RESULTS_DIR', '') == '':
        return {"return": 1, "error": "Please set --results_dir to the folder containing MLPerf inference results"}

    mlperf_path = env['CM_MLPERF_INFERENCE_SOURCE']
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)

    results_dir = env['CM_MLPERF_RESULTS_DIR']

    if env.get('CM_MLPERF_SUBMISSION_DIR', '') == '':
        from pathlib import Path
        user_home = str(Path.home())
        env['CM_MLPERF_SUBMISSION_DIR'] = os.path.join(user_home, "mlperf_submission")

    if env.get('CM_MLPERF_CLEAN_SUBMISSION_DIR','')!='':
        print ('=================================================')
        print ('Cleaning {} ...'.format(env['CM_MLPERF_SUBMISSION_DIR']))
        if os.path.exists(env['CM_MLPERF_SUBMISSION_DIR']):
            shutil.rmtree(env['CM_MLPERF_SUBMISSION_DIR'])
        print ('=================================================')

    submission_dir = env['CM_MLPERF_SUBMISSION_DIR']
    if not os.path.isdir(submission_dir):
        os.makedirs(submission_dir)

    print('* MLPerf inference submission dir: {}'.format(submission_dir))
    print('* MLPerf inference results dir: {}'.format(results_dir))
    results = [f for f in os.listdir(results_dir) if not os.path.isfile(os.path.join(results_dir, f))]

    system_meta = state['CM_SUT_META']

    if 'CM_MLPERF_SUBMISSION_SYSTEM_TYPE' in env:
        system_meta['system_type'] = env['CM_MLPERF_SUBMISSION_SYSTEM_TYPE']

    if 'CM_MLPERF_SUBMISSION_DIVISION' in env:
        system_meta['division'] = env['CM_MLPERF_SUBMISSION_DIVISION']

    if 'CM_MLPERF_SUBMISSION_CATEGORY' in env:
        system_meta['system_type'] = env['CM_MLPERF_SUBMISSION_CATEGORY']

    duplicate= (env.get('CM_MLPERF_DUPLICATE_SCENARIO_RESULTS', 'no') in ["yes", "True"])

    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') != '':
        division = env['CM_MLPERF_SUBMISSION_DIVISION']
        system_meta['division'] = division
    else:
        division = system_meta['division']

    if division not in ['open','closed']:
        return {'return':1, 'error':'"division" must be "open" or "closed"'}

    print('* MLPerf inference division: {}'.format(division))

    path_submission_root = submission_dir
    path_submission_division=os.path.join(path_submission_root, division)
    if not os.path.isdir(path_submission_division):
        os.makedirs(path_submission_division)

    # Check submitter
    if env.get('CM_MLPERF_SUBMITTER'):
        submitter = env['CM_MLPERF_SUBMITTER']
        system_meta['submitter'] = submitter
    else:
        submitter = system_meta['submitter']
        env['CM_MLPERF_SUBMITTER'] = submitter

    print('* MLPerf inference submitter: {}'.format(submitter))

    if 'Collective' not in system_meta.get('sw_notes'):
        system_meta['sw_notes'] =  "Automated by MLCommons CM v{}. ".format(cmind.__version__) + system_meta['sw_notes']

    if env.get('CM_MLPERF_SUT_SW_NOTES_EXTRA','') != '':
        sw_notes = f"{system_meta['sw_notes']} {env['CM_MLPERF_SUT_SW_NOTES_EXTRA']}"
        system_meta['sw_notes'] = sw_notes

    if env.get('CM_MLPERF_SUT_HW_NOTES_EXTRA','') != '':
        hw_notes = f"{system_meta['hw_notes']} {env['CM_MLPERF_SUT_HW_NOTES_EXTRA']}"
        system_meta['hw_notes'] = hw_notes

    path_submission=os.path.join(path_submission_division, submitter)
    if not os.path.isdir(path_submission):
        os.makedirs(path_submission)

    # SUT base
    system=env.get('CM_HW_NAME','default').replace(' ','_')

    code_path = os.path.join(path_submission, "code")

    for res in results:
        parts = res.split("-")
        if len(parts) > 5: #result folder structure used by CM script
            system = parts[0] if system == 'default' else system
            implementation = parts[1]
            device = parts[2]
            framework = parts[3]
            framework_version = parts[4]
            run_config = parts[5]

            print('* System: {}'.format(system))
            print('* Implementation: {}'.format(implementation))
            print('* Device: {}'.format(device))
            print('* Framework: {}'.format(framework))
            print('* Framework Version: {}'.format(framework_version))
            print('* Run Config: {}'.format(run_config))

            new_res = system + "-" + "-".join(parts[1:])

            # Override framework and framework versions from the folder name
            system_meta['framework'] = framework + " " + framework_version
        result_path = os.path.join(results_dir, res)
        platform_prefix = inp.get('platform_prefix', '')
        if platform_prefix:
            sub_res = platform_prefix + "-" + new_res
        else:
            sub_res = new_res

        submission_path = os.path.join(path_submission, "results", sub_res)
        measurement_path = os.path.join(path_submission, "measurements", sub_res)
        compliance_path = os.path.join(path_submission, "compliance", sub_res)
        system_path = os.path.join(path_submission, "systems")
        submission_system_path = system_path
        if not os.path.isdir(submission_system_path):
            os.makedirs(submission_system_path)
        system_file = os.path.join(submission_system_path, sub_res+".json")

        with open(system_file, "w") as fp:
            json.dump(system_meta, fp, indent=2)

        models = [f for f in os.listdir(result_path) if not os.path.isfile(os.path.join(result_path, f))]
        for model in models:
            result_model_path = os.path.join(result_path, model)
            submission_model_path = os.path.join(submission_path, model)
            measurement_model_path = os.path.join(measurement_path, model)
            compliance_model_path = os.path.join(compliance_path, model)
            code_model_path = os.path.join(code_path, model)
            scenarios = [f for f in os.listdir(result_model_path) if not os.path.isfile(os.path.join(result_model_path, f))]
            submission_code_path = code_model_path
            if not os.path.isdir(submission_code_path):
                os.makedirs(submission_code_path)
            if not os.path.exists(os.path.join(submission_code_path, "README.md")):
                with open(os.path.join(submission_code_path, "README.md"), mode='w') as f:
                    f.write("TBD") #create an empty README

            print('* MLPerf inference model: {}'.format(model))
            for scenario in scenarios:
                result_scenario_path = os.path.join(result_model_path, scenario)
                submission_scenario_path = os.path.join(submission_model_path, scenario)
                measurement_scenario_path = os.path.join(measurement_model_path, scenario)
                compliance_scenario_path = os.path.join(compliance_model_path, scenario)

                if duplicate and scenario=='singlestream':
                    if not os.path.exists(os.path.join(result_model_path, "offline")):
                        print('Duplicating results from {} to offline:'.format(scenario))
                        shutil.copytree(result_scenario_path, os.path.join(result_model_path, "offline"))
                        scenarios.append("offline")
                    if not os.path.exists(os.path.join(result_model_path, "multistream")):
                        print('Duplicating results from {} to multistream:'.format(scenario))
                        shutil.copytree(result_scenario_path, os.path.join(result_model_path, "multistream"))
                        scenarios.append("multistream")

                modes = [f for f in os.listdir(result_scenario_path) if not os.path.isfile(os.path.join(result_scenario_path, f))]
                power_run = False
                for mode in modes:
                    result_mode_path = os.path.join(result_scenario_path, mode)
                    submission_mode_path = os.path.join(submission_scenario_path, mode)
                    submission_measurement_path = measurement_scenario_path
                    submission_compliance_path = os.path.join(compliance_scenario_path, mode)
                    if mode.startswith("TEST"):
                        submission_results_path = submission_compliance_path
                    else:
                        submission_results_path = submission_mode_path
                    if os.path.exists(submission_results_path):
                        shutil.rmtree(submission_results_path)

                    if not os.path.isdir(submission_measurement_path):
                        os.makedirs(submission_measurement_path)

                    if mode=='performance':

                        if os.path.exists(os.path.join(result_mode_path, "power")):
                            power_run = True
                            result_power_path=os.path.join(result_mode_path, 'power')
                            submission_power_path=os.path.join(submission_mode_path, 'power')
                            os.makedirs(submission_power_path)
                            power_files = []
                            for f in os.listdir(result_power_path):
                                power_files.append(f) #Todo add required check from submission_checker
                            for f in power_files:
                                shutil.copy(os.path.join(result_power_path, f), os.path.join(submission_power_path, f))

                            analyzer_settings_file = env.get('CM_MLPERF_POWER_ANALYZER_SETTINGS_FILE_PATH', os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "analyzer_table.md"))
                            power_settings_file = env.get('CM_MLPERF_POWER_SETTINGS_FILE_PATH', os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "power_settings.md"))

                            shutil.copy(analyzer_settings_file, os.path.join(submission_measurement_path, "analyzer_table.md"))
                            shutil.copy(power_settings_file, os.path.join(submission_measurement_path, "power_settings.md"))

                            result_ranging_path=os.path.join(result_mode_path, 'ranging')
                            submission_ranging_path=os.path.join(submission_mode_path, 'ranging')
                            os.makedirs(submission_ranging_path)
                            ranging_files = []
                            for f in os.listdir(result_ranging_path):
                                ranging_files.append(f) #Todo add required check from submission_checker
                            for f in ranging_files:
                                shutil.copy(os.path.join(result_ranging_path, f), os.path.join(submission_ranging_path, f))

                        result_mode_path=os.path.join(result_mode_path, 'run_1')
                        submission_results_path=os.path.join(submission_mode_path, 'run_1')

                    if not os.path.isdir(submission_results_path):
                        os.makedirs(submission_results_path)

                    #if division == "closed" and not os.path.isdir(submission_compliance_path):
                    #    os.makedirs(submission_compliance_path)

                    mlperf_inference_conf_path = os.path.join(result_mode_path, "mlperf.conf")
                    if os.path.exists(mlperf_inference_conf_path):
                        shutil.copy(mlperf_inference_conf_path, os.path.join(submission_measurement_path, 'mlperf.conf'))
                    user_conf_path = os.path.join(result_mode_path, "user.conf")
                    if os.path.exists(user_conf_path):
                        shutil.copy(user_conf_path, os.path.join(submission_measurement_path, 'user.conf'))
                    measurements_json_path = os.path.join(result_mode_path, "measurements.json")
                    if os.path.exists(user_conf_path):
                        shutil.copy(measurements_json_path, os.path.join(submission_measurement_path, sub_res+'.json'))
                    files = []
                    readme = False

                    for f in os.listdir(result_mode_path):
                        if mode.startswith("TEST"):
                            if f.startswith('verify_'):
                                files.append(f)
                            elif f == "performance":
                                compliance_performance_run_path = os.path.join(result_mode_path, f, "run_1")
                                if os.path.exists(compliance_performance_run_path):
                                    target = os.path.join(submission_results_path, "performance", "run_1")
                                    os.makedirs(target)
                                    for log_file in os.listdir(compliance_performance_run_path):
                                        if log_file.startswith("mlperf_"):
                                            shutil.copy(os.path.join(compliance_performance_run_path, log_file), os.path.join(target, log_file))
                            elif f == "accuracy":
                                compliance_accuracy_run_path = os.path.join(result_mode_path, f)
                                if os.path.exists(compliance_accuracy_run_path):
                                    target = os.path.join(submission_results_path, "accuracy")
                                    os.makedirs(target)
                                    for log_file in os.listdir(compliance_accuracy_run_path):
                                        if log_file.startswith("mlperf_log_accuracy.json") or log_file.endswith("accuracy.txt"):
                                            shutil.copy(os.path.join(compliance_accuracy_run_path, log_file), os.path.join(target, log_file))
                        else:
                            if f.startswith('mlperf_') and not f.endswith('trace.json'):
                                files.append(f)
                            elif f == "spl.txt":
                                files.append(f)
                            elif f in [ "README.md", "README-extra.md", "cm-version-info.json", "os_info.json", "cpu_info.json", "pip_freeze.json" ] and mode == "performance":
                                shutil.copy(os.path.join(result_mode_path, f), os.path.join(submission_measurement_path, f))
                            elif f in [ "console.out" ]:
                                shutil.copy(os.path.join(result_mode_path, f), os.path.join(submission_measurement_path, mode+"_"+f))


                    if mode == "accuracy":
                        if os.path.exists(os.path.join(result_mode_path, "accuracy.txt")):
                            files.append("accuracy.txt")
                        if model == "stable-diffusion-xl" and os.path.exists(os.path.join(result_mode_path, "images")):
                            shutil.copytree(os.path.join(result_mode_path, "images"), os.path.join(submission_results_path, "images"))

                    for f in files:
                        print(' * ' + f)
                        p_target = os.path.join(submission_results_path, f)
                        shutil.copy(os.path.join(result_mode_path, f), p_target)

                readme_file = os.path.join(submission_measurement_path, "README.md")
                if not os.path.exists(readme_file):
                    with open(readme_file, mode='w') as f:
                        f.write("TBD") #create an empty README
                else:
                    readme_suffix = ""
                    result_string = get_result_string(env['CM_MLPERF_LAST_RELEASE'], model, scenario, result_scenario_path, power_run)
                    with open(readme_file, mode='a') as f:
                        f.write(result_string)


    return {'return':0}


def get_accuracy_metric(config, model, path):

    import submission_checker as checker
    import re
    is_valid = False
    all_accuracy_valid = True
    acc = None
    result_acc = None
    target = config.get_accuracy_target(model)
    acc_upper_limit = config.get_accuracy_upper_limit(model)
    patterns = []
    acc_targets = []
    acc_limits = []
    up_patterns = []
    acc_types = []

    if acc_upper_limit is not None:
        acc_limit_check = True
        for i in range(0, len(acc_upper_limit), 2):
            acc_type, acc_target = acc_upper_limit[i:i+2]
            acc_limits.append(acc_target)
            up_patterns.append(checker.ACC_PATTERN[acc_type])

    for i in range(0, len(target), 2):
        acc_type, acc_target = target[i:i+2]
        acc_types.append(acc_type)
        patterns.append(checker.ACC_PATTERN[acc_type])
        acc_targets.append(acc_target)

    acc_seen = [False for _ in acc_targets]
    acc_results = {}
    with open(os.path.join(path, "accuracy.txt"), "r", encoding="utf-8") as f:
        for line in f:
            for i, (pattern, acc_target, acc_type) in enumerate(zip(patterns, acc_targets, acc_types)):
                m = re.match(pattern, line)
                if m:
                    acc = m.group(1)

                    acc_results[acc_type] = acc

                if acc is not None and float(acc) >= acc_target:
                    all_accuracy_valid &= True
                    acc_seen[i] = True
                elif acc is not None:
                    all_accuracy_valid = False
                    #log.warning("%s accuracy not met: expected=%f, found=%s", path, acc_target, acc)
                if i == 0 and acc:
                    result_acc = acc
                acc = None
            if acc_upper_limit is not None:
                for i, (pattern, acc_limit) in enumerate(zip(up_patterns, acc_limits)):
                    m = re.match(pattern, line)
                    if m:
                        acc = m.group(1)
                    if acc is not None and acc_upper_limit is not None and float(acc) > acc_limit:
                        acc_limit_check = False
                        #log.warning("%s accuracy not met: upper limit=%f, found=%s", path, acc_limit, acc)
                    acc = None
            if all(acc_seen):
                break;
        is_valid = all_accuracy_valid & all(acc_seen)
        if acc_upper_limit is not None:
            is_valid &= acc_limit_check


    return acc_results, acc_targets, acc_limits, up_patterns


def get_result_string(version, model, scenario, result_path, has_power):
    import submission_checker as checker
    config = checker.Config(
        version,
        None,
        ignore_uncommited=False,
        skip_power_check=False,
    )
    mlperf_model = config.get_mlperf_model(model)
    performance_path = os.path.join(result_path, "performance", "run_1")
    accuracy_path = os.path.join(result_path, "accuracy")
    scenario = checker.SCENARIO_MAPPING[scenario]

    performance_result = checker.get_performance_metric(config, mlperf_model, performance_path, scenario, None, None, has_power)
    if has_power:
        is_valid, power_metric, scenario, avg_power_efficiency = checker.get_power_metric(config, scenario, performance_path, True, performance_result)
        if "stream" in scenario.lower():
            power_metric_unit = "milliJoules"
        else:
            power_metric_unit = "Watts"
        power_result_string = f"`Power consumed`: `{round(power_metric, 5)} {power_metric_unit}`, `Power efficiency`: `{round(avg_power_efficiency * 1000, 5)} samples per Joule`"

    acc_results, acc_targets, acc_limits, up_patterns = get_accuracy_metric(config, mlperf_model, accuracy_path)

    result_field = checker.RESULT_FIELD[scenario]

    performance_result_string = f"`{result_field}`: `{performance_result}`\n"
    accuracy_result_string = ''
    for i, acc in enumerate(acc_results):
        accuracy_result_string += f"`{acc}`: `{round(float(acc_results[acc]), 5)}`"
        if not up_patterns:
            accuracy_result_string += f", Required accuracy for closed division `>= {round(acc_targets[i], 5)}`"
        else:
            accuracy_result_string += f", Required accuracy for closed division `>= {round(acc_targets[i], 5)}` and `<= {round(acc_limits[i], 5)}`"
        accuracy_result_string += "\n"

    result_string = "\n\n## Results \n"
    result_string += "### Accuracy Results \n" + accuracy_result_string
    result_string += "\n### Performance Results \n" + performance_result_string
    if has_power:
        result_string += "\n### Power Results \n" + power_result_string

    return result_string
 
def postprocess(i):

    r = generate_submission(i)
    if r['return'] > 0:
        return r

    return {'return':0}
