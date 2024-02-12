from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    pip_freeze = {}
    if os.path.isfile('tmp-pip-freeze'):
        with open("tmp-pip-freeze", "r") as f:
            for line in f.readlines():
                if "==" in line:
                    split = line.split("==")
                    pip_freeze[split[0]] = split[1].strip() 

    state['pip_freeze'] = pip_freeze

    return {'return':0}
