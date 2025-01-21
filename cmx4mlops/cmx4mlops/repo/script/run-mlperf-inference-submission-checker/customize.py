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
import cmind as cm
import os
import subprocess


def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    q = '"' if os_info['platform'] == 'windows' else "'"

    submission_dir = env.get("CM_MLPERF_INFERENCE_SUBMISSION_DIR", "")

    version = env.get('CM_MLPERF_SUBMISSION_CHECKER_VERSION', '')

    if submission_dir == "":
        return {'return': 1,
                'error': 'Please set --env.CM_MLPERF_INFERENCE_SUBMISSION_DIR'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "")  # "default")
    if ' ' in submitter:
        return {
            'return': 1, 'error': 'CM_MLPERF_SUBMITTER cannot contain a space. Please provide a name without space using --submitter input. Given value: {}'.format(submitter)}

    if 'CM_MLPERF_SKIP_COMPLIANCE' in env:
        skip_compliance = " --skip_compliance"
    else:
        skip_compliance = ""

    submission_checker_file = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
                                           "submission_checker.py")

    if env['CM_MLPERF_SHORT_RUN'] == "yes":
        import shutil
        new_submission_checker_file = os.path.join(
            os.path.dirname(submission_checker_file),
            "submission_checker1.py")
        with open(submission_checker_file, 'r') as file:
            data = file.read()
        data = data.replace("OFFLINE_MIN_SPQ = 24576", "OFFLINE_MIN_SPQ = 100")
        data = data.replace(
            "return is_valid, res, inferred",
            "return True, res, inferred")
        with open(new_submission_checker_file, 'w') as file:
            file.write(data)
        submission_checker_file = new_submission_checker_file

    if env.get('CM_MLPERF_EXTRA_MODEL_MAPPING', '') != '':
        extra_map = ' --extra_model_benchmark_map "' + \
            env['CM_MLPERF_EXTRA_MODEL_MAPPING'] + '"'
    else:
        extra_map = ""

    if env.get('CM_MLPERF_SKIP_POWER_CHECK', 'no') == "yes":
        power_check = " --skip-power-check"
    else:
        power_check = ""

    extra_args = ' ' + env.get('CM_MLPERF_SUBMISSION_CHECKER_EXTRA_ARGS', '')

    x_submitter = ' --submitter ' + q + submitter + q if submitter != '' else ''

    x_version = ' --version ' + version + ' ' if version != '' else ''

    CMD = env['CM_PYTHON_BIN_WITH_PATH'] + ' ' + q + submission_checker_file + q + ' --input ' + q + submission_dir + q + \
        x_submitter + \
        x_version + \
        skip_compliance + extra_map + power_check + extra_args

    x_version = ' --version ' + version[1:] + ' ' if version != '' else ''

    x_submission_repo_name = ''
    x_submission_repo_owner = ''
    x_submission_repo_branch = ''

    if env.get('CM_MLPERF_RESULTS_GIT_REPO_NAME', '') != '':
        x_submission_repo_name = f""" --repository {env['CM_MLPERF_RESULTS_GIT_REPO_NAME']}"""
    if env.get('CM_MLPERF_RESULTS_GIT_REPO_OWNER', '') != '':
        x_submission_repo_owner = f""" --repository-owner {env['CM_MLPERF_RESULTS_GIT_REPO_OWNER']}"""
    if env.get('CM_MLPERF_RESULTS_GIT_REPO_BRANCH', '') != '':
        x_submission_repo_branch = f""" --repository-branch  {env['CM_MLPERF_RESULTS_GIT_REPO_BRANCH']}"""

    report_generator_file = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
                                         "generate_final_report.py")
    env['CM_RUN_CMD'] = CMD
    print(CMD)
    env['CM_POST_RUN_CMD'] = env['CM_PYTHON_BIN_WITH_PATH'] + ' ' + q + report_generator_file + q + ' --input summary.csv ' + \
        x_version + \
        x_submission_repo_name + \
        x_submission_repo_owner + \
        x_submission_repo_branch

    return {'return': 0}


def postprocess(i):

    env = i['env']
    if env.get('CM_TAR_SUBMISSION_DIR', ''):
        env['CM_TAR_INPUT_DIR'] = env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']

    x = env.get('MLPERF_INFERENCE_SUBMISSION_TAR_FILE', '')
    if x != '':
        env['CM_TAR_OUTFILE'] = x

    if env.get('CM_MLPERF_INFERENCE_SUBMISSION_BASE_DIR', '') != '':
        env['CM_TAR_OUTPUT_DIR'] = env['CM_MLPERF_INFERENCE_SUBMISSION_BASE_DIR']

    x = env.get('MLPERF_INFERENCE_SUBMISSION_SUMMARY', '')
    if x != '':
        for y in ['.csv', '.json', '.xlsx']:

            z0 = 'summary' + y

            if os.path.isfile(z0):
                z1 = x + y

                if os.path.isfile(z1):
                    os.remove(z1)

                os.rename(z0, z1)

    return {'return': 0}
