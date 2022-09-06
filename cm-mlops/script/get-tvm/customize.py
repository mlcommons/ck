from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']

    tvm_home = env['TVM_HOME']

    if '+PYTHONPATH' not in env: env['+PYTHONPATH']=[]
    env['+PYTHONPATH'].append(os.path.join(tvm_home,'python'))

    return {'return':0}
