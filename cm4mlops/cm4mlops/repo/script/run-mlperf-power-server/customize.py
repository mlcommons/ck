#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import cmind as cm
import os
import configparser


def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    # Initialize ConfigParser
    config = configparser.ConfigParser()

    if env.get('CM_MLPERF_POWER_SERVER_CONF_FILE', '') != '':
        server_config_file = env['CM_MLPERF_POWER_SERVER_CONF_FILE']
    else:
        server_config_file = os.path.join(
            env.get('CM_MLPERF_POWER_SOURCE', ''),
            'ptd_client_server',
            'server.template.conf'
        )

    # Read the configuration file with error handling
    if not os.path.exists(server_config_file):
        raise FileNotFoundError(
            f"Server config file not found: {server_config_file}")

    config.read(server_config_file)
    # Update the server section
    try:
        config['server']['ntpServer'] = env['CM_MLPERF_POWER_NTP_SERVER']
        config['server']['listen'] = f"{env['CM_MLPERF_POWER_SERVER_ADDRESS']} {env['CM_MLPERF_POWER_SERVER_PORT']}"
    except KeyError as e:
        raise KeyError(f"Missing required environment variable: {e}")

    # Define number of analyzers and network port start
    num_analyzers = int(env.get('CM_MLPERF_POWER_NUM_ANALYZERS', 1))
    network_port_start = int(
        env.get(
            'CM_MLPERF_POWER_NETWORK_PORT_START',
            8888))

    # Ensure 'ptd' section exists
    if 'ptd' not in config:
        config.add_section('ptd')

    config['ptd']['ptd'] = str(env.get('CM_MLPERF_PTD_PATH', ''))
    config['ptd']['analyzercount'] = str(num_analyzers)

    # Add analyzers to the configuration
    for aid in range(1, num_analyzers + 1):
        analyzer_section = f'analyzer{aid}'
        if analyzer_section not in config:
            config.add_section(analyzer_section)

            # Add the analyzer subsection as keys under the 'ptd' section
            config[f'{analyzer_section}']['interfaceFlag'] = str(
                env.get('CM_MLPERF_POWER_INTERFACE_FLAG', ''))
            config[f'{analyzer_section}']['deviceType'] = str(
                env.get('CM_MLPERF_POWER_DEVICE_TYPE', ''))
            config[f'{analyzer_section}']['devicePort'] = str(
                env.get('CM_MLPERF_POWER_DEVICE_PORT', ''))
            config[f'{analyzer_section}']['networkPort'] = str(
                network_port_start + aid - 1)

    with open('tmp-power-server.conf', 'w') as configfile:
        config.write(configfile)

    print({section: dict(config[section]) for section in config.sections()})

    if env['CM_HOST_OS_TYPE'] == "windows":
        cmd_prefix = ""
    else:
        cmd_prefix = "sudo "

    cmd = env['CM_PYTHON_BIN_WITH_PATH'] + ' ' + os.path.join(
        env['CM_MLPERF_POWER_SOURCE'],
        'ptd_client_server',
        'server.py') + ' -c tmp-power-server.conf'
    if env.get('CM_MLPERF_POWER_SERVER_USE_SCREEN', 'no') == 'yes':
        cmd = cmd_prefix + ' screen -d -m ' + cmd + ' '
    else:
        cmd = cmd_prefix + cmd

    env['RUN_CMD'] = cmd

    return {'return': 0}


def postprocess(i):
    return {'return': 0}
