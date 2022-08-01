from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    #print(i['state'])
    if 'CM_LOADGEN_QPS' not in env:
        env['CM_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_LOADGEN_QPS_OPT'] = " --qps " + env['CM_LOADGEN_QPS']
    if 'CM_LOADGEN_SCENARIO' not in env:
        env['CM_LOADGEN_SCENARIO'] = "Offline"
    if 'CM_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_LOADGEN_EXTRA_OPTIONS'] = ""
    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_LOADGEN_QPS_OPT']

    return {'return':0}
