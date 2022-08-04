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
        return {'return': -1}
    submitter = env.get("CM_MLC_SUBMITTER", "default")
    os.system("rm -rf " + submission_dir + "_logs")
    CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "tools", "submission",
            "truncate_accuracy_log.py") + " --input " + submission_dir + " --submitter " + submitter + " --backup " + submission_dir + "_logs"
    print(CMD)
    ret = os.system(CMD)

    return {'return':ret}
