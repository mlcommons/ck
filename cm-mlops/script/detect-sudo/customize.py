from cmind import utils
import os, subprocess

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if prompt_sudo() == 0:
        env['CM_SUDO_USER'] = "yes"

    return {'return':0}

def prompt_sudo():
    if os.geteuid() != 0:
        msg = "[sudo] password for %u:"
        return subprocess.check_call("sudo echo 'Check sudo' -p '%s'" % msg, shell=True)
    return -1


def postprocess(i):

    env = i['env']

    return {'return':0}
