from cmind import utils
import cmind as cm
import os
import subprocess

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLPERF_SUBMISSION_DIR", "")

    version = env.get('CM_MLPERF_SUBMISSION_CHECKER_VERSION','v3.1')
    
    if submission_dir == "":
        return {'return': 1, 'error': 'Please set CM_MLPERF_SUBMISSION_DIR'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "") #"default")
    if ' ' in submitter:
        return {'return': 1, 'error': 'CM_MLPERF_SUBMITTER cannot contain a space. Please provide a name without space using --submitter input. Given value: {}'.format(submitter)}

    submission_checker_file = os.path.join(env['CM_MLPERF_LOGGING_REPO_PATH'], "scripts", "verify_for_" + version  + "_training.sh")

    extra_args = ' ' + env.get('CM_MLPERF_SUBMISSION_CHECKER_EXTRA_ARGS','')

    CMD = submission_checker_file + " " + submission_dir

    env['CM_RUN_CMD'] = CMD

    return {'return':0}

def postprocess(i):

    env = i['env']
    if env.get('CM_TAR_SUBMISSION_DIR'):
        env['CM_TAR_INPUT_DIR'] = env.get('CM_MLPERF_SUBMISSION_DIR', '$HOME')

    return {'return':0}
