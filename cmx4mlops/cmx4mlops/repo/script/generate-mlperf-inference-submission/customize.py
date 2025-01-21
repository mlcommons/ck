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
import cmind
import sys
from tabulate import tabulate
import mlperf_utils


def preprocess(i):
    return {'return': 0}

# Helper function to fill dictionary from JSON file


def fill_from_json(file_path, keys, sut_info):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for key in keys:
            if key in data and (
                    sut_info[key] is None or sut_info[key] == "default"):
                sut_info[key] = data[key]
            elif key in data and sut_info[key] != data[key]:
                return -1  # error saying there is a mismatch in the value of a key
        return sut_info

# Helper function to check whether all the keys(sut information) are assigned


def check_dict_filled(keys, sut_info):
    for key in keys:
        if key in sut_info and sut_info[key] is None:
            return False
    return True

# The function checks whether the submitting model name belongs standard
# model names for MLPef Inference


def model_in_valid_models(model, mlperf_version):
    import submission_checker as checker
    config = checker.MODEL_CONFIG

    if model not in config[mlperf_version]['models']:
        internal_model_name = config[mlperf_version]["model_mapping"].get(
            model, '')  # resnet50 -> resnet
        if internal_model_name == '':
            # Indicate failure with no internal model name
            return (False, None)
        else:
            # Indicate success with internal model name
            return (True, internal_model_name)
    else:
        return (True, model)


def generate_submission(env, state, inp, submission_division):

    # Save current user directory
    cur_dir = os.getcwd()

    if env.get('CM_MLPERF_INFERENCE_RESULTS_DIR_', '') == '':
        results_dir = os.path.join(
            env['CM_MLPERF_INFERENCE_RESULTS_DIR'],
            f"{env['CM_MLPERF_RUN_STYLE']}_results")
    else:
        results_dir = env['CM_MLPERF_INFERENCE_RESULTS_DIR_']

    mlperf_path = env['CM_MLPERF_INFERENCE_SOURCE']
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)

    if env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '') == '':
        from pathlib import Path
        user_home = str(Path.home())
        env['CM_MLPERF_INFERENCE_SUBMISSION_DIR'] = os.path.join(
            user_home, "mlperf_submission")

    submission_dir = env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '')
    if submission_dir == '':
        submission_base_dir = env.get(
            'CM_MLPERF_INFERENCE_SUBMISSION_BASE_DIR', '')
        if submission_base_dir == '':
            return {'return': 1, 'error': f"Both CM_MLPERF_INFERENCE_SUBMISSION_DIR and CM_MLPERF_INFERENCE_SUBMISSION_BASE_DIR can not be empty!"}
        else:
            submission_dir = os.path.join(
                submission_base_dir, "mlperf_inference_submission")
            env['CM_MLPERF_INFERENCE_SUBMISSION_DIR'] = submission_dir

    if env.get('CM_MLPERF_CLEAN_SUBMISSION_DIR', '') != '':
        print('=================================================')
        print(
            'Cleaning {} ...'.format(
                env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']))
        if os.path.exists(submission_dir):
            shutil.rmtree(submission_dir)
        print('=================================================')

    if not os.path.isdir(submission_dir):
        os.makedirs(submission_dir)

    if str(env.get('CM_MLPERF_SUBMISSION_DIR_SHARED', '')
           ).lower() in ["yes", "true", "1"]:
        os.chmod(submission_dir, 0o2775)

    print('* MLPerf inference submission dir: {}'.format(submission_dir))
    print('* MLPerf inference results dir: {}'.format(results_dir))
    results = [
        f for f in os.listdir(results_dir) if not os.path.isfile(
            os.path.join(
                results_dir,
                f))]

    system_meta_default = state['CM_SUT_META']

    # set pytorch as the default framework
    if system_meta_default['framework'] == '':
        system_meta_default['framework'] = "pytorch"

    system_meta_tmp = {}
    if 'CM_MLPERF_SUBMISSION_SYSTEM_TYPE' in env:
        system_meta_tmp['system_type'] = env['CM_MLPERF_SUBMISSION_SYSTEM_TYPE']

    if submission_division != "":
        system_meta_tmp['division'] = submission_division
        division = submission_division
    else:
        division = system_meta_default['division']

    if 'CM_MLPERF_SUBMISSION_CATEGORY' in env:
        system_meta_tmp['system_type'] = env['CM_MLPERF_SUBMISSION_CATEGORY'].replace(
            "-", ",")

    duplicate = (
        env.get(
            'CM_MLPERF_DUPLICATE_SCENARIO_RESULTS',
            'no') in [
            "yes",
            "True"])

    if division not in ['open', 'closed']:
        return {'return': 1, 'error': '"division" must be "open" or "closed"'}

    print('* MLPerf inference division: {}'.format(division))

    path_submission_root = submission_dir
    path_submission_division = os.path.join(path_submission_root, division)
    if not os.path.isdir(path_submission_division):
        os.makedirs(path_submission_division)

    # Check submitter
    if env.get('CM_MLPERF_SUBMITTER'):
        submitter = env['CM_MLPERF_SUBMITTER']
        system_meta_tmp['submitter'] = submitter
    else:
        submitter = system_meta_default['submitter']
        env['CM_MLPERF_SUBMITTER'] = submitter

    print('* MLPerf inference submitter: {}'.format(submitter))

    if env.get('CM_MLPERF_SUT_SW_NOTES_EXTRA', '') != '':
        sw_notes = f"{system_meta_tmp['sw_notes']} {env['CM_MLPERF_SUT_SW_NOTES_EXTRA']}"
        system_meta_tmp['sw_notes'] = sw_notes

    if env.get('CM_MLPERF_SUT_HW_NOTES_EXTRA', '') != '':
        hw_notes = f"{system_meta_tmp['hw_notes']} {env['CM_MLPERF_SUT_HW_NOTES_EXTRA']}"
        system_meta_tmp['hw_notes'] = hw_notes

    path_submission = os.path.join(path_submission_division, submitter)
    if not os.path.isdir(path_submission):
        os.makedirs(path_submission)

    # SUT base
    system = env.get('CM_HW_NAME', 'default').replace(' ', '_')

    code_path = os.path.join(path_submission, "code")

    for res in results:
        system_meta = {}
        system_meta.update(system_meta_tmp)
        result_path = os.path.join(results_dir, res)
        # variable to check whether the sut_meta.json is present in the root
        # folder
        saved_system_meta_file_path = os.path.join(
            result_path, 'system_meta.json')
        # checks for json file containing system meta
        sut_info = {
            "hardware_name": None,
            "implementation": None,
            "device": None,
            "framework": None,
            "framework_version": "default",
            "run_config": "default"
        }  # variable to store the system meta

        model_mapping_combined = {}  # to store all the model mapping related to an SUT

        # check whether the root folder contains the sut infos
        # if yes then there is no need to check for meta files inside
        # individual model folders
        if "cm-sut-info.json" in os.listdir(result_path):
            sut_info = fill_from_json(
                os.path.join(
                    result_path,
                    "cm-sut-info.json"),
                sut_info.keys(),
                sut_info)
            if sut_info == -1:
                return {
                    'return': 1, 'error': f"key value mismatch. Refer the populating dictionary:\n{sut_info}\n and file {os.path.join(result_path, 'cm-sut-info.json')}"}
            if check_dict_filled(sut_info.keys(), sut_info):
                print(
                    f"sut info completely filled from {os.path.join(result_path, 'cm-sut-info.json')}!")

        # Check whether the root folder contains the model mapping file
        # expects json file in the format:
        # {
        #   custom_model1:official_model(could be any official model),
        #   custom_model2:official_model(could be any official model)
        # }
        if "model_mapping.json" in os.listdir(result_path):
            with open(os.path.join(result_path, "model_mapping.json"), 'r') as f:
                model_mapping_combined = json.load(f)

        # Preprocessing part.
        # Even the model mapping json file is present in root directory, the folders are traversed
        # and the data is updated provided not duplicated.
        models = [
            f for f in os.listdir(result_path) if not os.path.isfile(
                os.path.join(
                    result_path, f))]
        if division == "open" and len(model_mapping_combined) == 0:
            for model in models:
                is_valid, returned_model_name = model_in_valid_models(
                    model, env.get('CM_MLPERF_LAST_RELEASE', 'v4.1'))
                if not is_valid:
                    result_model_path = os.path.join(result_path, model)
                    scenarios = [
                        f for f in os.listdir(result_model_path) if not os.path.isfile(
                            os.path.join(
                                result_model_path, f))]
                    for scenario in scenarios:
                        result_scenario_path = os.path.join(
                            result_model_path, scenario)
                        modes = [
                            f for f in os.listdir(result_scenario_path) if not os.path.isfile(
                                os.path.join(
                                    result_scenario_path, f))]
                        for mode in modes:
                            result_mode_path = os.path.join(
                                result_scenario_path, mode)
                            if mode == "performance":
                                compliance_performance_run_path = os.path.join(
                                    result_mode_path, "run_1")
                                # model mapping part
                                tmp_model_mapping_file_path = os.path.join(
                                    compliance_performance_run_path, "model_mapping.json")
                                if os.path.exists(tmp_model_mapping_file_path):
                                    with open(tmp_model_mapping_file_path, 'r') as f:
                                        new_model_mapping = json.load(f)
                                        for new_custom_model in new_model_mapping:
                                            if new_custom_model not in model_mapping_combined:
                                                model_mapping_combined.update(
                                                    {new_custom_model: new_model_mapping[new_custom_model]})
                                else:
                                    return {
                                        "return": 1, "error": f"model_mapping.json not found in {compliance_performance_run_path}"}
                else:
                    if returned_model_name != model:
                        model_mapping_combined.update(
                            {model: returned_model_name})

        if check_dict_filled(sut_info.keys(), sut_info):
            system = sut_info["hardware_name"]
            implementation = sut_info["implementation"]
            device = sut_info["device"]
            framework = sut_info["framework"].replace(" ", "_")
            framework_version = sut_info["framework_version"]
            run_config = sut_info["run_config"]
            new_res = f"{system}-{implementation}-{device}-{framework}-{run_config}"
        else:
            new_res = res

        print(f"The SUT folder name for submission generation is: {new_res}")

        platform_prefix = inp.get('platform_prefix', '')
        if platform_prefix:
            sub_res = platform_prefix + "-" + new_res
        else:
            sub_res = new_res

        submission_path = os.path.join(path_submission, "results", sub_res)
        measurement_path = os.path.join(
            path_submission, "measurements", sub_res)
        compliance_path = os.path.join(path_submission, "compliance", sub_res)
        system_path = os.path.join(path_submission, "systems")
        submission_system_path = system_path

        if not os.path.isdir(submission_system_path):
            os.makedirs(submission_system_path)
        system_file = os.path.join(submission_system_path, sub_res + ".json")

        # Save the model mapping json file
        if model_mapping_combined:
            with open(os.path.join(path_submission, "model_mapping.json"), "w") as fp:
                json.dump(model_mapping_combined, fp, indent=2)

        models = [
            f for f in os.listdir(result_path) if not os.path.isfile(
                os.path.join(
                    result_path, f))]

        results = {}

        model_platform_info_file = None

        for model in models:
            results[model] = {}
            platform_info_file = None
            result_model_path = os.path.join(result_path, model)
            submission_model_path = os.path.join(submission_path, model)
            measurement_model_path = os.path.join(measurement_path, model)
            compliance_model_path = os.path.join(compliance_path, model)
            code_model_path = os.path.join(code_path, model)
            scenarios = [
                f for f in os.listdir(result_model_path) if not os.path.isfile(
                    os.path.join(
                        result_model_path, f))]
            submission_code_path = code_model_path
            if not os.path.isdir(submission_code_path):
                os.makedirs(submission_code_path)
            if not os.path.exists(os.path.join(
                    submission_code_path, "README.md")):
                with open(os.path.join(submission_code_path, "README.md"), mode='w') as f:
                    f.write("TBD")  # create an empty README

            print('* MLPerf inference model: {}'.format(model))
            for scenario in scenarios:
                # the system_info.txt is copied from the mode directory if
                # found, else it would be looked under scenario directory
                system_info_from_mode = False
                results[model][scenario] = {}
                result_scenario_path = os.path.join(
                    result_model_path, scenario)
                submission_scenario_path = os.path.join(
                    submission_model_path, scenario)
                measurement_scenario_path = os.path.join(
                    measurement_model_path, scenario)
                compliance_scenario_path = os.path.join(
                    compliance_model_path, scenario)

                if duplicate and scenario == 'singlestream':
                    if not os.path.exists(os.path.join(
                            result_model_path, "offline")):
                        print(
                            'Duplicating results from {} to offline:'.format(scenario))
                        shutil.copytree(
                            result_scenario_path, os.path.join(
                                result_model_path, "offline"))
                        scenarios.append("offline")
                    if not os.path.exists(os.path.join(
                            result_model_path, "multistream")):
                        print(
                            'Duplicating results from {} to multistream:'.format(scenario))
                        shutil.copytree(
                            result_scenario_path, os.path.join(
                                result_model_path, "multistream"))
                        scenarios.append("multistream")

                modes = [
                    f for f in os.listdir(result_scenario_path) if not os.path.isfile(
                        os.path.join(
                            result_scenario_path, f))]
                power_run = False

                # we check for the existance of mlperf_log_summary.txt
                # mlperf_log_detail.txt to consider a result folder as valid.
                # Rest of the checks are done later by the submission checker
                files_to_check = [
                    "mlperf_log_summary.txt",
                    "mlperf_log_detail.txt"]
                if not all([os.path.exists(os.path.join(
                        result_scenario_path, "performance", "run_1", f)) for f in files_to_check]):
                    continue

                if not os.path.isdir(measurement_scenario_path):
                    os.makedirs(measurement_scenario_path)

                for mode in modes:
                    result_mode_path = os.path.join(result_scenario_path, mode)
                    submission_mode_path = os.path.join(
                        submission_scenario_path, mode)
                    submission_measurement_path = measurement_scenario_path
                    submission_compliance_path = os.path.join(
                        compliance_scenario_path, mode)
                    if mode.startswith("TEST"):
                        submission_results_path = submission_compliance_path
                    else:
                        submission_results_path = submission_mode_path
                    if os.path.exists(submission_results_path):
                        shutil.rmtree(submission_results_path)

                    if mode == 'performance':

                        if os.path.exists(os.path.join(
                                result_mode_path, "power")):
                            power_run = True
                            result_power_path = os.path.join(
                                result_mode_path, 'power')
                            submission_power_path = os.path.join(
                                submission_mode_path, 'power')
                            os.makedirs(submission_power_path)
                            power_files = []
                            for f in os.listdir(result_power_path):
                                # Todo add required check from
                                # submission_checker
                                power_files.append(f)
                            for f in power_files:
                                shutil.copy(
                                    os.path.join(
                                        result_power_path, f), os.path.join(
                                        submission_power_path, f))

                            analyzer_settings_file = env.get(
                                'CM_MLPERF_POWER_ANALYZER_SETTINGS_FILE_PATH', os.path.join(
                                    env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "analyzer_table.md"))
                            power_settings_file = env.get(
                                'CM_MLPERF_POWER_SETTINGS_FILE_PATH', os.path.join(
                                    env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "power_settings.md"))

                            shutil.copy(
                                analyzer_settings_file, os.path.join(
                                    submission_measurement_path, "analyzer_table.md"))
                            shutil.copy(
                                power_settings_file, os.path.join(
                                    submission_measurement_path, "power_settings.md"))

                            result_ranging_path = os.path.join(
                                result_mode_path, 'ranging')
                            submission_ranging_path = os.path.join(
                                submission_mode_path, 'ranging')
                            os.makedirs(submission_ranging_path)
                            ranging_files = []
                            for f in os.listdir(result_ranging_path):
                                # Todo add required check from
                                # submission_checker
                                ranging_files.append(f)
                            for f in ranging_files:
                                shutil.copy(
                                    os.path.join(
                                        result_ranging_path, f), os.path.join(
                                        submission_ranging_path, f))

                        result_mode_path = os.path.join(
                            result_mode_path, 'run_1')
                        submission_results_path = os.path.join(
                            submission_mode_path, 'run_1')

                        if not os.path.exists(saved_system_meta_file_path):
                            if os.path.exists(os.path.join(
                                    result_mode_path, "system_meta.json")):
                                saved_system_meta_file_path = os.path.join(
                                    result_mode_path, "system_meta.json")
                            else:
                                print("WARNING: system_meta.json was not found in the SUT root or mode directory inside the results folder. CM is automatically creating one using the system defaults. Please modify them as required.")
                        if os.path.exists(saved_system_meta_file_path):
                            with open(saved_system_meta_file_path, "r") as f:
                                saved_system_meta = json.load(f)
                                for key in list(saved_system_meta):
                                    if saved_system_meta[key] is None or str(
                                            saved_system_meta[key]).strip() == '':
                                        del (saved_system_meta[key])
                                if saved_system_meta["division"] != "" and submission_division == "":
                                    system_meta["division"] = saved_system_meta["division"]
                                # override the saved meta with the user inputs
                                system_meta = {
                                    **saved_system_meta, **system_meta}
                        # add any missing fields from the defaults, if
                        # system_meta.json is not detected, default one will be
                        # written
                        system_meta = {**system_meta_default, **system_meta}
                        print(system_meta)
                        # check if framework version is there in system_meta,
                        # if not try to fill it from sut_info
                        if system_meta['framework'] == "":
                            system_meta['framework'] = sut_info.get(
                                'framework', '') + sut_info.get('framework_version', '')
                            if system_meta['framework'] == "":
                                print(
                                    "WARNING: framework field could not be filled from system_meta.json or sut_info.json. This will trigger error in submission checker")

                    if not os.path.isdir(submission_results_path):
                        os.makedirs(submission_results_path)

                    # if division == "closed" and not os.path.isdir(submission_compliance_path):
                    #    os.makedirs(submission_compliance_path)

                    user_conf_path = os.path.join(
                        result_scenario_path, "user.conf")
                    if os.path.exists(user_conf_path):
                        shutil.copy(
                            user_conf_path, os.path.join(
                                measurement_scenario_path, 'user.conf'))
                    else:
                        user_conf_path = os.path.join(
                            result_mode_path, "user.conf")
                        if os.path.exists(user_conf_path):
                            shutil.copy(
                                user_conf_path, os.path.join(
                                    submission_measurement_path, 'user.conf'))
                        else:
                            if mode.lower() == "performance":
                                return {
                                    "return": 1, "error": f"user.conf missing in both paths: {user_conf_path} and {os.path.join(result_scenario_path, 'user.conf')}"}

                    measurements_json_path = os.path.join(
                        result_scenario_path, "measurements.json")
                    target_measurement_json_path = measurement_scenario_path
                    if not os.path.exists(measurements_json_path):
                        measurements_json_path = os.path.join(
                            result_mode_path, "measurements.json")
                        target_measurement_json_path = submission_measurement_path

                    if os.path.exists(measurements_json_path):
                        with open(measurements_json_path, "r") as f:
                            measurements_json = json.load(f)
                            model_precision = measurements_json.get(
                                "weight_data_types", "fp32")
                        shutil.copy(
                            measurements_json_path,
                            os.path.join(
                                target_measurement_json_path,
                                sub_res + '.json'))
                        shutil.copy(
                            measurements_json_path,
                            os.path.join(
                                target_measurement_json_path,
                                'model-info.json'))
                    else:
                        if mode.lower() == "performance":
                            return {
                                "return": 1, "error": f"measurements.json missing in both paths: {measurements_json_path} and {os.path.join(result_scenario_path, 'user.conf')}"}

                    files = []
                    readme = False

                    for f in os.listdir(result_mode_path):
                        if mode.startswith("TEST"):
                            if f.startswith('verify_'):
                                files.append(f)
                            elif f == "performance":
                                compliance_performance_run_path = os.path.join(
                                    result_mode_path, f, "run_1")
                                if os.path.exists(
                                        compliance_performance_run_path):
                                    target = os.path.join(
                                        submission_results_path, "performance", "run_1")
                                    os.makedirs(target)
                                    for log_file in os.listdir(
                                            compliance_performance_run_path):
                                        if log_file.startswith("mlperf_"):
                                            shutil.copy(
                                                os.path.join(
                                                    compliance_performance_run_path, log_file), os.path.join(
                                                    target, log_file))
                            elif f == "accuracy":
                                compliance_accuracy_run_path = os.path.join(
                                    result_mode_path, f)
                                if os.path.exists(
                                        compliance_accuracy_run_path):
                                    target = os.path.join(
                                        submission_results_path, "accuracy")
                                    os.makedirs(target)
                                    for log_file in os.listdir(
                                            compliance_accuracy_run_path):
                                        if log_file.startswith(
                                                "mlperf_log_accuracy.json") or log_file.endswith("accuracy.txt"):
                                            shutil.copy(
                                                os.path.join(
                                                    compliance_accuracy_run_path, log_file), os.path.join(
                                                    target, log_file))
                        else:
                            if f.startswith('mlperf_') and not f.endswith(
                                    'trace.json'):
                                files.append(f)
                            elif f == "spl.txt":
                                files.append(f)
                            elif f in ["README.md", "README-extra.md", "cm-version-info.json", "os_info.json", "cpu_info.json", "pip_freeze.json", "system_info.txt", "cm-deps.png", "cm-deps.mmd"] and mode == "performance":
                                shutil.copy(
                                    os.path.join(
                                        result_mode_path, f), os.path.join(
                                        submission_measurement_path, f))
                                if f == "system_info.txt" and not platform_info_file:
                                    # the first found system_info.txt will be taken as platform info file for a specific model to be placed in
                                    # measurements-model folder when generating
                                    # the final submission
                                    platform_info_file = os.path.join(
                                        result_mode_path, f)
                            elif f in ["console.out"]:
                                shutil.copy(
                                    os.path.join(
                                        result_mode_path, f), os.path.join(
                                        submission_measurement_path, mode + "_" + f))

                    if mode == "accuracy":
                        if os.path.exists(os.path.join(
                                result_mode_path, "accuracy.txt")):
                            files.append("accuracy.txt")
                        if model == "stable-diffusion-xl" and os.path.exists(
                                os.path.join(result_mode_path, "images")):
                            shutil.copytree(
                                os.path.join(
                                    result_mode_path, "images"), os.path.join(
                                    submission_results_path, "images"))

                    for f in files:
                        print(' * ' + f)
                        p_target = os.path.join(submission_results_path, f)
                        shutil.copy(
                            os.path.join(
                                result_mode_path,
                                f),
                            p_target)

                if os.path.exists(os.path.join(
                        result_scenario_path, "system_info.txt")):
                    shutil.copy(
                        os.path.join(
                            result_scenario_path, "system_info.txt"), os.path.join(
                            submission_measurement_path, f))
                    platform_info_file = os.path.join(
                        result_scenario_path, "system_info.txt")

                readme_file = os.path.join(
                    submission_measurement_path, "README.md")
                if not os.path.exists(readme_file):
                    with open(readme_file, mode='w') as f:
                        f.write("TBD")  # create an empty README

                readme_suffix = ""
                result_string, result = mlperf_utils.get_result_string(
                    env['CM_MLPERF_LAST_RELEASE'], model, scenario, result_scenario_path, power_run, sub_res, division, system_file, model_precision, env.get('CM_MLPERF_INFERENCE_SOURCE_VERSION'))

                for key in result:
                    results[model][scenario][key] = result[key]
                with open(readme_file, mode='a') as f:
                    f.write(result_string)

            # Copy system_info.txt to the submission measurements model folder
            # if any scenario performance run has it
            sys_info_file = None

            if os.path.exists(os.path.join(
                    result_model_path, "system_info.txt")):
                sys_info_file = os.path.join(
                    result_model_path, "system_info.txt")
            elif platform_info_file:
                sys_info_file = platform_info_file

            if sys_info_file:
                model_platform_info_file = sys_info_file
                shutil.copy(
                    sys_info_file,
                    os.path.join(
                        measurement_model_path,
                        "system_info.txt"))

        # Copy system_info.txt to the submission measurements folder if any
        # model performance run has it
        sys_info_file = None

        if os.path.exists(os.path.join(result_path, "system_info.txt")):
            sys_info_file = os.path.join(result_path, "system_info.txt")
        elif model_platform_info_file:
            sys_info_file = model_platform_info_file

        if sys_info_file:
            shutil.copy(
                sys_info_file,
                os.path.join(
                    measurement_path,
                    "system_info.txt"))
        else:
            if env.get('CM_GET_PLATFORM_DETAILS', '') == "yes":
                cm_input = {'action': 'run',
                            'automation': 'script',
                            'tags': 'get,platform,details',
                            'env': {'CM_PLATFORM_DETAILS_FILE_PATH': os.path.join(measurement_path, "system_info.txt")},
                            'quiet': True
                            }
                r = cmind.access(cm_input)
                if r['return'] > 0:
                    return r

        with open(system_file, "w") as fp:
            json.dump(system_meta, fp, indent=2)

        result_table, headers = mlperf_utils.get_result_table(results)

        print(tabulate(result_table, headers=headers, tablefmt="pretty"))

        sut_readme_file = os.path.join(measurement_path, "README.md")
        with open(sut_readme_file, mode='w') as f:
            f.write(tabulate(result_table, headers=headers, tablefmt="github"))

    return {'return': 0}


def postprocess(i):
    env = i['env']
    state = i['state']
    inp = i['input']

    submission_divisions = []

    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') in [
            "open-closed", "closed-open"]:
        submission_divisions = ["open", "closed"]
    elif env.get('CM_MLPERF_SUBMISSION_DIVISION', '') != '':
        submission_divisions.append(env['CM_MLPERF_SUBMISSION_DIVISION'])

    # if submission division is not assigned, default value would be taken in
    # submission_generation function
    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') == '':
        r = generate_submission(env, state, inp, submission_division="")
    else:
        for submission_division in submission_divisions:
            r = generate_submission(env, state, inp, submission_division)
            if r['return'] > 0:
                return r

    return {'return': 0}
