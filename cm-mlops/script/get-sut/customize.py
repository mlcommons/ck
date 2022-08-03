from cmind import utils
import os
import json

def preprocess(i):
    env = i['env']
    state = i['state']
    if 'CM_SUT_NAME' not in env:
        env['CM_SUT_NAME'] = "dummy"
    sut = env['CM_SUT_NAME']
    path = i['run_script_input']['path']
    sut_path = os.path.join(path, "suts", sut + ".json")
    if os.path.exists(sut_path):
        state['CM_SUT_META'] = json.load(open(sut_path))
    else:
        print("SUT description file not present")
        return {'return':-1}
    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
