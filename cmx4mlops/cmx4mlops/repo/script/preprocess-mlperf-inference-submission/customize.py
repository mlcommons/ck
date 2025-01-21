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
from os.path import exists
import shutil


def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLPERF_INFERENCE_SUBMISSION_DIR", "")

    if submission_dir == "":
        print("Please set --env.CM_MLPERF_INFERENCE_SUBMISSION_DIR")
        return {'return': 1,
                'error': 'CM_MLPERF_INFERENCE_SUBMISSION_DIR is not specified'}

    if not os.path.exists(submission_dir):
        print("Please set --env.CM_MLPERF_INFERENCE_SUBMISSION_DIR to a valid submission directory")
        return {'return': 1,
                'error': 'CM_MLPERF_INFERENCE_SUBMISSION_DIR is not existing'}

    submission_dir = submission_dir.rstrip(os.path.sep)
    submitter = env.get("CM_MLPERF_SUBMITTER", "MLCommons")
    submission_processed = f"{submission_dir}_processed"

    if os.path.exists(submission_processed):
        print(f"Cleaning {submission_processed}")
        shutil.rmtree(submission_processed)

    CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
                                                     "preprocess_submission.py") + "' --input '" + submission_dir + "' --submitter '" + submitter + "' --output '" + submission_processed + "'"
    env['CM_RUN_CMD'] = CMD

    return {'return': 0}


def postprocess(i):

    env = i['env']
    submission_dir = env["CM_MLPERF_INFERENCE_SUBMISSION_DIR"]
    import datetime
    submission_backup = submission_dir + "_backup_" + \
        '{date:%Y-%m-%d_%H:%M:%S}'.format(date=datetime.datetime.now())

    submission_processed = submission_dir + "_processed"
    shutil.copytree(submission_dir, submission_backup)
    shutil.rmtree(submission_dir)
    os.rename(submission_processed, submission_dir)

    return {'return': 0}
