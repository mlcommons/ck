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
    config['ptd']['interfaceFlag'] = env['CM_MLPERF_POWER_INTERFACE_FLAG']
    config['ptd']['deviceType'] = env['CM_MLPERF_POWER_DEVICE_TYPE']
    config['ptd']['devicePort'] = env['CM_MLPERF_POWER_DEVICE_PORT']
    with open('power-server.conf', 'w') as configfile:
        config.write(configfile)
    print({section: dict(config[section]) for section in config.sections()})

    return {'return':0}

def postprocess(i):
    return {'return':0}
