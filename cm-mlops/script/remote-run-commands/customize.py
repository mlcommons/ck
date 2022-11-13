from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    cmd_string=''
    run_cmds = env.get('CM_SSH_RUN_COMMANDS', [])
    for i,cmd in enumerate(run_cmds):
        if 'cm ' in cmd:
            cmd=cmd.replace(":", "=")
            cmd=cmd.replace(";;", ",")
            run_cmds[i] = cmd
    cmd_string += " ; ".join(run_cmds)
    user = env.get('CM_SSH_USER')
    password = env.get('CM_SSH_PASSWORD', None)
    host = env.get('CM_SSH_HOST')
    if password:
        password_string = " -p "+password
    else:
        password_string = ""
    cmd_extra = ''
    if env.get("CM_SSH_SKIP_HOST_VERIFY"):
        cmd_extra += " -o StrictHostKeyChecking=no"
    if env.get("CM_SSH_KEY_FILE"):
        cmd_extra += " -i "+env.get("CM_SSH_KEY_FILE")
    ssh_command = "ssh "+user+"@"+host+password_string+ cmd_extra + " '"+cmd_string + "'"
    env['CM_SSH_CMD'] = ssh_command

    return {'return':0}

def postprocess(i):

    return {'return':0}


