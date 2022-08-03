from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLC_SUBMISSION_DIR", "")
    if submission_dir == "":
        print("Please set CM_MLC_SUBMISSION_DIR")
        exit(-1)
    submitter = env.get("CM_MLC_SUBMITTER", "dummy")
    CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "tools", "submission",
            "submission-checker.py") + " --input " + submission_dir + " --submitter " + submitter + " --skip_compliance"
    os.system(CMD)

    return {'return':0}
