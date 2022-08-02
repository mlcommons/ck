from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    #print(i['state'])
    if 'CM_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_LOADGEN_EXTRA_OPTIONS'] = ""
    if 'CM_LOADGEN_MODE' not in env:
        env['CM_LOADGEN_MODE'] = "performance"
    elif env['CM_LOADGEN_MODE'] == "accuracy":
        env['CM_LOADGEN_EXTRA_OPTIONS'] += " --accuracy"

    if 'CM_LOADGEN_QPS' not in env:
        env['CM_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_LOADGEN_QPS_OPT'] = " --qps " + env['CM_LOADGEN_QPS']
    if 'CM_LOADGEN_SCENARIO' not in env:
        env['CM_LOADGEN_SCENARIO'] = "Offline"
    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_LOADGEN_QPS_OPT']
    if 'OUTPUT_DIR' not in env:
        env['OUTPUT_DIR'] =  os.path.join(os.getcwd() , env['CM_BACKEND'] + "-" + env['CM_DEVICE'], env['CM_MODEL'],
        env['CM_LOADGEN_SCENARIO'].lower(), env['CM_LOADGEN_MODE'])

    return {'return':0}
