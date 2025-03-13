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
import cmind as cm


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    cmd = env.get('CM_GH_ACTIONS_RUNNER_COMMAND', '')
    if cmd == "config":
        run_cmd = f"cd {env['CM_GH_ACTIONS_RUNNER_CODE_PATH']} && ./config.sh --url {env['CM_GH_ACTIONS_RUNNER_URL']} --token {env['CM_GH_ACTIONS_RUNNER_TOKEN']}"
    elif cmd == "remove":
        run_cmd = f"cd {env['CM_GH_ACTIONS_RUNNER_CODE_PATH']} && ./config.sh remove --token {env['CM_GH_ACTIONS_RUNNER_TOKEN']}"
    elif cmd == "install":
        run_cmd = f"cd {env['CM_GH_ACTIONS_RUNNER_CODE_PATH']} && sudo ./svc.sh install"
    elif cmd == "uninstall":
        run_cmd = f"cd {env['CM_GH_ACTIONS_RUNNER_CODE_PATH']} && sudo ./svc.sh uninstall"
        cache_rm_tags = "gh,runner,_install"
        r = cm.access({'action': 'rm', 'automation': 'cache',
                      'tags': cache_rm_tags, 'f': True})
        print(r)
        if r['return'] != 0 and r['return'] != 16:  # ignore missing ones
            return r
    elif cmd == "start":
        run_cmd = f"cd {env['CM_GH_ACTIONS_RUNNER_CODE_PATH']} && sudo ./svc.sh start"

    env['CM_RUN_CMD'] = run_cmd

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
