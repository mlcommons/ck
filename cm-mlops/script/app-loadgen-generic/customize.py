from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if 'CM_ML_MODEL_FILE_WITH_PATH' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}

    env['CM_RUN_OPTS'] = ''
    run_opts = ''
    if 'CM_MLPERF_RUNNER' in env:
        run_opts +=" -r "+env['CM_MLPERF_RUNNER']
    if 'CM_MLPERF_CONCURRENCY' in env:
        run_opts +=" --concurrency "+env['CM_MLPERF_CONCURRENCY']
    if 'CM_MLPERF_EXECUTION_PROVIDER' in env:
        run_opts +=" --ep "+env['CM_MLPERF_EXECUTION_PROVIDER']
    if 'CM_MLPERF_INTRAOP' in env:
        run_opts +=" --intraop "+env['CM_MLPERF_INTRAOP']
    if 'CM_MLPERF_INTEROP' in env:
        run_opts +=" --interop "+env['CM_MLPERF_INTEROP']
    if 'CM_MLPERF_EXECMODE' in env:
        run_opts +=" --execmode "+env['CM_MLPERF_EXECUTION_MODE']
    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}
