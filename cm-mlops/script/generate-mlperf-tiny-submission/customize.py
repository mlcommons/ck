from cmind import utils
import os
import json
import shutil

def preprocess(i):
    return generate_submission(i)


##############################################################################

def generate_submission(i):

    # Save current user directory
    cur_dir=os.getcwd()
    env = i['env']
    state = i['state']
    inp=i['input']
    results_dir = env['CM_MLPERF_RESULTS_DIR']

    if 'CM_MLPERF_SUBMISSION_DIR' not in env:
        env['CM_MLPERF_SUBMISSION_DIR'] = os.path.join(cur_dir, "results")
    submission_dir = env['CM_MLPERF_SUBMISSION_DIR']
    if not os.path.isdir(submission_dir):
        os.makedirs(submission_dir)

    print('* MLPerf tiny submission dir: {}'.format(submission_dir))
    print('* MLPerf tiny results dir: {}'.format(results_dir))
    results = [f for f in os.listdir(results_dir) if not os.path.isfile(os.path.join(results_dir, f))]

    division=inp.get('division','open')

    if division not in ['open','closed']:
        return {'return':1, 'error':'"division" must be "open" or "closed"'}
    system_meta = state['CM_SUT_META']
    division = system_meta['division']

    print('* MLPerf tiny division: {}'.format(division))

    path_submission_root = submission_dir
    path_submission_division=os.path.join(path_submission_root, division)
    if not os.path.isdir(path_submission_division):
        os.makedirs(path_submission_division)

    # Check submitter
    submitter = system_meta['submitter']
    env['CM_MLPERF_SUBMITTER'] = submitter

    print('* MLPerf tiny submitter: {}'.format(submitter))

    path_submission=os.path.join(path_submission_division, submitter)
    if not os.path.isdir(path_submission):
        os.makedirs(path_submission)

    # SUT base
    system=i.get('system','default')

    code_path = os.path.join(path_submission, "code")
    for res in results:
        parts = res.split("-")
        backend = parts[0]
        target = parts[1]
        framework = backend

        print('* Target: {}'.format(target))
        print('* Framework: {}'.format(framework))
        result_path = os.path.join(results_dir, res)
        platform_prefix = inp.get('platform_prefix', '')
        if platform_prefix:
            sub_res = platform_prefix + "-" + res
        else:
            sub_res = res
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
                with open(os.path.join(submission_code_path, "README.md"), mode='w'): pass #create an empty README

            print('* MLPerf inference model: {}'.format(model))
            for scenario in scenarios:
                result_scenario_path = os.path.join(result_model_path, scenario)
                submission_scenario_path = os.path.join(submission_model_path, scenario)
                measurement_scenario_path = os.path.join(measurement_model_path, scenario)
                compliance_scenario_path = os.path.join(compliance_model_path, scenario)
                
                modes = [f for f in os.listdir(result_scenario_path) if not os.path.isfile(os.path.join(result_scenario_path, f))]
                for mode in modes:
                    result_mode_path = os.path.join(result_scenario_path, mode)
                    submission_mode_path = os.path.join(submission_scenario_path, mode)
                    submission_results_path = submission_mode_path
                    submission_measurement_path = measurement_scenario_path
                    submission_compliance_path = os.path.join(compliance_scenario_path, mode)
                    if mode=='performance':
                        result_mode_path=os.path.join(result_mode_path, 'run_1')
                        submission_results_path=os.path.join(submission_mode_path, 'run_1')
                    if not os.path.isdir(submission_results_path):
                        os.makedirs(submission_results_path)
                    if not os.path.isdir(submission_measurement_path):
                        os.makedirs(submission_measurement_path)
                    if not os.path.isdir(submission_compliance_path):
                        os.makedirs(submission_compliance_path)
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
                        if f.startswith('mlperf_'):
                            files.append(f)
                        if f == "README.md":
                            shutil.copy(os.path.join(result_mode_path, f), os.path.join(submission_measurement_path, f))
                            readme = True

                    if mode == "accuracy":
                        if os.path.exists(os.path.join(result_mode_path, "accuracy.txt")):
                            files.append("accuracy.txt")

                    for f in files:
                        print(' * ' + f)
                        p_target = os.path.join(submission_results_path, f)
                        shutil.copy(os.path.join(result_mode_path, f), p_target)

                    if not readme:
                        with open(os.path.join(submission_measurement_path, "README.md"), mode='w'): pass #create an empty README

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
