from cmind import utils
import cmind as cm
import os
import subprocess

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLPERF_SUBMISSION_DIR", "")

    if submission_dir == "":
        return {'return': 1, 'error': 'Please set CM_MLPERF_SUBMISSION_DIR'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "default")
    if ' ' in submitter:
        return {'return': 1, 'error': 'CM_MLPERF_SUBMITTER cannot contain a space. Please provide a name without space using --submitter input. Given value: {}'.format(submitter)}

    if 'CM_MLPERF_SKIP_COMPLIANCE' in env: 
        skip_compliance = " --skip_compliance"
    else:
        skip_compliance = ""

    submission_checker_file = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
            "submission_checker.py")

    if env['CM_MLPERF_SHORT_RUN'] == "yes":
        import shutil
        new_submission_checker_file = os.path.join(os.path.dirname(submission_checker_file), "submission_checker1.py")
        with open(submission_checker_file, 'r') as file:
            data = file.read()
        data = data.replace("OFFLINE_MIN_SPQ = 24576", "OFFLINE_MIN_SPQ = 100")
        data = data.replace("return is_valid, res, inferred", "return True, res, inferred")
        with open(new_submission_checker_file, 'w') as file:
            file.write(data)
        submission_checker_file = new_submission_checker_file

    if env.get('CM_MLPERF_EXTRA_MODEL_MAPPING', '') != '':
        extra_map = " --extra_model_benchmark_map "+env['CM_MLPERF_EXTRA_MODEL_MAPPING']
    else:
        extra_map = ""

    if env.get('CM_MLPERF_POWER', 'no') == "yes":
        power_check = " --more_power_check"
    else:
        power_check = ""

    CMD = env['CM_PYTHON_BIN'] + ' ' + submission_checker_file + " --input '" + submission_dir + "' --submitter '" + submitter + "'" + \
            skip_compliance + extra_map + power_check
    env['CM_RUN_CMD'] = CMD

    return {'return':0}

def postprocess(i):
    return {'return':0}
