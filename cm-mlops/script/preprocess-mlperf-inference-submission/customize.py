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
        print("Please set CM_MLPERF_INFERENCE_SUBMISSION_DIR")
        return {'return': 1, 'error':'CM_MLPERF_INFERENCE_SUBMISSION_DIR is not specified'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "cTuning")
    submission_processed = submission_dir + "_processed"

    if os.path.exists(submission_processed):
        shutil.rmtree(submission_processed)

    os.system("rm -rf " + submission_dir + "_processed")

    CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
            "preprocess_submission.py") + "' --input '" + submission_dir + "' --submitter '" + submitter + "' --output '" + submission_processed + "'"
    env['CM_RUN_CMD'] = CMD

    return {'return':0}

def postprocess(i):

    env = i['env']
    submission_dir = env["CM_MLPERF_INFERENCE_SUBMISSION_DIR"]
    import datetime
    submission_backup = submission_dir+"_backup_"+'{date:%Y-%m-%d_%H:%M:%S}'.format( date=datetime.datetime.now() )

    submission_processed = submission_dir + "_processed"
    shutil.copytree(submission_dir, submission_backup)
    shutil.rmtree(submission_dir)
    os.rename(submission_processed, submission_dir)

    return {'return':0}
