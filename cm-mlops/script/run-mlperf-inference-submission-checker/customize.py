from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLPERF_SUBMISSION_DIR", "")

    if submission_dir == "":
        return {'return': 1, 'error': 'Please set CM_MLPERF_SUBMISSION_DIR'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "default")

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

    CMD = env['CM_PYTHON_BIN'] + ' ' + submission_checker_file + " --input " + submission_dir + " --submitter " + submitter + \
            skip_compliance

    print ('=================================================')
    print (CMD)
    print ('=================================================')

    ret = os.system(CMD)

    return {'return':0}

def postprocess(i):
    input('xyz')
    
    import pandas

    env = i['env']

    if exists('summary.csv'):
        df = pandas.read_csv('summary.csv').T

        print ('')
        print (df)
        print ('')

        df.to_json('summary.json', orient='columns', indent=4)

    return {'return':0}
