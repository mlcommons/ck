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
import os


def preprocess(i):
    os_info = i['os_info']
    env = i['env']

    q = '"' if os_info['platform'] == 'windows' else "'"

    if env.get('CM_RUN_CMD', '') == '':
        if env.get('CM_BIN_NAME', '') == '':
            x = 'run.exe' if os_info['platform'] == 'windows' else 'run.out'
            env['CM_BIN_NAME'] = x

        if os_info['platform'] == 'windows':
            env['CM_RUN_CMD'] = env.get(
                'CM_RUN_PREFIX', '') + env['CM_BIN_NAME']
            if env.get('CM_RUN_SUFFIX', '') != '':
                env['CM_RUN_CMD'] += ' ' + env['CM_RUN_SUFFIX']

        else:
            if env['CM_ENABLE_NUMACTL'].lower() in ["on", "1", "true", "yes"]:
                env['CM_ENABLE_NUMACTL'] = "1"
                CM_RUN_PREFIX = "numactl " + env['CM_NUMACTL_MEMBIND'] + ' '
            else:
                CM_RUN_PREFIX = ''

            CM_RUN_PREFIX += env.get('CM_RUN_PREFIX', '')

            env['CM_RUN_PREFIX'] = CM_RUN_PREFIX

            CM_RUN_SUFFIX = (
                env['CM_REDIRECT_OUT'] +
                ' ') if 'CM_REDIRECT_OUT' in env else ''
            CM_RUN_SUFFIX += (env['CM_REDIRECT_ERR'] +
                              ' ') if 'CM_REDIRECT_ERR' in env else ''

            env['CM_RUN_SUFFIX'] = env['CM_RUN_SUFFIX'] + \
                CM_RUN_SUFFIX if 'CM_RUN_SUFFIX' in env else CM_RUN_SUFFIX

            if env.get('CM_RUN_DIR', '') == '':
                env['CM_RUN_DIR'] = os.getcwd()

            env['CM_RUN_CMD'] = CM_RUN_PREFIX + ' ' + os.path.join(
                env['CM_RUN_DIR'], env['CM_BIN_NAME']) + ' ' + env['CM_RUN_SUFFIX']

    x = env.get('CM_RUN_PREFIX0', '')
    if x != '':
        env['CM_RUN_CMD'] = x + ' ' + env.get('CM_RUN_CMD', '')

    if os_info['platform'] != 'windows' and str(
            env.get('CM_SAVE_CONSOLE_LOG', True)).lower() not in ["no", "false", "0"]:
        logs_dir = env.get('CM_LOGS_DIR', env['CM_RUN_DIR'])
        env['CM_RUN_CMD'] += r" 2>&1 | tee " + q + os.path.join(
            logs_dir, "console.out") + q + r"; echo \${PIPESTATUS[0]} > exitstatus"

    # additional arguments and tags for measuring system informations(only if
    # 'CM_PROFILE_NVIDIA_POWER' is 'on')
    if env.get('CM_PROFILE_NVIDIA_POWER', '') == "on":
        env['CM_SYS_UTILISATION_SCRIPT_TAGS'] = ''
        # this section is for selecting the variation
        if env.get('CM_MLPERF_DEVICE', '') == "gpu":
            env['CM_SYS_UTILISATION_SCRIPT_TAGS'] += ',_cuda'
        elif env.get('CM_MLPERF_DEVICE', '') == "cpu":
            env['CM_SYS_UTILISATION_SCRIPT_TAGS'] += ',_cpu'
        # this section is for supplying the input arguments/tags
        env['CM_SYS_UTILISATION_SCRIPT_TAGS'] += ' --log_dir=\'' + \
            logs_dir + '\''   # specify the logs directory
        # specifying the interval in which the system information should be
        # measured
        if env.get('CM_SYSTEM_INFO_MEASUREMENT_INTERVAL', '') != '':
            env['CM_SYS_UTILISATION_SCRIPT_TAGS'] += ' --interval=\"' + \
                env['CM_SYSTEM_INFO_MEASUREMENT_INTERVAL'] + '\"'

    # generate the pre run cmd - recording runtime system infos
    pre_run_cmd = ""

    if env.get('CM_PRE_RUN_CMD_EXTERNAL', '') != '':
        pre_run_cmd += env['CM_PRE_RUN_CMD_EXTERNAL']

    if env.get('CM_PROFILE_NVIDIA_POWER', '') == "on":
        if pre_run_cmd != '':
            pre_run_cmd += ' && '

        # running the script as a process in background
        pre_run_cmd = pre_run_cmd + 'cm run script --tags=runtime,system,utilisation' + \
            env['CM_SYS_UTILISATION_SCRIPT_TAGS'] + ' --quiet  & '
        # obtain the command if of the background process
        pre_run_cmd += r" cmd_pid=\$!  && echo CMD_PID=\$cmd_pid"
        print(
            f"Pre run command for recording the runtime system information: {pre_run_cmd}")

    env['CM_PRE_RUN_CMD'] = pre_run_cmd

    # generate the post run cmd - for killing the process that records runtime
    # system infos
    post_run_cmd = ""
    if env.get('CM_PROFILE_NVIDIA_POWER', '') == "on":
        post_run_cmd += r"echo killing process \$cmd_pid && kill -TERM \${cmd_pid}"
        print(
            f"Post run command for killing the process that measures the runtime system information: {post_run_cmd}")

    env['CM_POST_RUN_CMD'] = post_run_cmd

    # Print info
    print('***************************************************************************')
    print('CM script::benchmark-program/run.sh')
    print('')
    print('Run Directory: {}'.format(env.get('CM_RUN_DIR', '')))

    print('')
    print('CMD: {}'.format(env.get('CM_RUN_CMD', '')))

    print('')

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
