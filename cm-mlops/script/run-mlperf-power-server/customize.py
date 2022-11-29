from cmind import utils
import cmind as cm
import os
import configparser

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    config = configparser.ConfigParser()
    server_config_file = os.path.join(env['CM_MLPERF_POWER_SOURCE'], 'ptd_client_server', 'server.template.conf')
    config.read(server_config_file)
    config['server']['ntpServer'] = env['CM_MLPERF_POWER_NTP_SERVER']
    config['ptd']['ptd'] = env['CM_MLPERF_PTD_PATH']
    config['server']['outDir'] = env['CM_MLPERF_POWER_SERVER_OUTDIR']
    config['ptd']['logFile'] = env['CM_MLPERF_POWER_LOG_FILE']
    with open('power-server.conf', 'w') as configfile:
        config.write(configfile)

    return {'return':0}

def postprocess(i):
    return {'return':0}
