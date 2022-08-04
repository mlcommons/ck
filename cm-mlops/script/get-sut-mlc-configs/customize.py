from cmind import utils
import os
import yaml

def preprocess(i):
    env = i['env']
    state = i['state']
    if 'CM_SUT_NAME' not in env:
        env['CM_SUT_NAME'] = "default"
    sut = env['CM_SUT_NAME']
    path = i['run_script_input']['path']
    config_path = os.path.join(path, "configs", env['CM_SUT_NAME'], "config.yaml")
    if not os.path.exists(config_path):
        print("SUT config file not present")
        return {'return':-1}
    if 'CM_SUT_CONFIG' not in state:
        state['CM_SUT_CONFIG'] = {}
    state['CM_SUT_CONFIG'][env['CM_SUT_NAME']] = yaml.load(open(config_path))
    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
