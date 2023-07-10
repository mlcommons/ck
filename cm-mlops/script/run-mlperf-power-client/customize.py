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

    if 'CM_MLPERF_LOADGEN_LOGS_DIR' not in env:
        env['CM_MLPERF_LOADGEN_LOGS_DIR'] = os.path.join(os.getcwd(), "loadgen_logs")

    run_cmd = env['CM_MLPERF_RUN_CMD'].replace("'", '"')
    run_cmd = run_cmd.replace('"', '\\"')
    cmd = env['CM_PYTHON_BIN_WITH_PATH'] + ' ' +\
            os.path.join(env['CM_MLPERF_POWER_SOURCE'], 'ptd_client_server', 'client.py') + \
            " -a " + env['CM_MLPERF_POWER_SERVER_ADDRESS'] + \
            " -p " + env.get('CM_MLPERF_POWER_SERVER_PORT', "4950") + \
            " -w '" + run_cmd + \
            "' -L " + env['CM_MLPERF_LOADGEN_LOGS_DIR'] + \
            " -o " + env['CM_MLPERF_POWER_LOG_DIR'] + \
            " -n " + env['CM_MLPERF_POWER_NTP_SERVER'] + \
            timestamp

    if 'CM_MLPERF_POWER_MAX_AMPS' in env and 'CM_MLPERF_POWER_MAX_VOLTS' in env:
           cmd = cmd + " --max-amps " + env['CM_MLPERF_POWER_MAX_AMPS'] + \
                " --max-volts " + env['CM_MLPERF_POWER_MAX_VOLTS']

    env['CM_MLPERF_POWER_RUN_CMD'] = cmd

    return {'return':0}

def postprocess(i):
    return {'return':0}
