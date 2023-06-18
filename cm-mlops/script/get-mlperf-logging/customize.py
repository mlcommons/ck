from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    meta = i['meta']

    env['CM_MLPERF_LOGGING_SRC_PATH'] = env['CM_GIT_REPO_CHECKOUT_PATH']

    return {'return':0}

def postprocess(i):
    env = i['env']

    env['+PYTHONPATH'] = [ env['CM_MLPERF_LOGGING_SRC_PATH'] ]

    return {'return':0}
