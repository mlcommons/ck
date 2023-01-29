from cmind import utils
import cmind as cm
import os
import configparser

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if not env['CM_MLPERF_RUN_CMD']:
        env['CM_MLPERF_RUN_CMD'] = os.path.join(i['run_script_input']['path'], "dummy.sh")

    if 'CM_MLPERF_POWER_TIMESTAMP' in env:
        timestamp = ""
    else:
        timestamp = " --no-timestamp-path"

    cmd = env['CM_PYTHON_BIN_WITH_PATH'] + ' ' +\
            os.path.join(env['CM_MLPERF_POWER_SOURCE'], 'ptd_client_server', 'client.py') + \
            " -a " + env['CM_MLPERF_POWER_SERVER_ADDRESS'] + \
            " -w '" + env['CM_MLPERF_RUN_CMD'].replace("'", "\"") + \
            "' -L " + env['CM_MLPERF_LOADGEN_LOGS_DIR'] + \
            " -o " + env['CM_MLPERF_POWER_LOG_DIR'] + \
            " -n " + env['CM_MLPERF_POWER_NTP_SERVER'] + \
            " --max-amps " + env['CM_MLPERF_POWER_MAX_AMPS'] + \
            " --max-volts " + env['CM_MLPERF_POWER_MAX_VOLTS'] + \
            timestamp

    env['CM_MLPERF_POWER_RUN_CMD'] = cmd

    return {'return':0}

def postprocess(i):
    return {'return':0}
