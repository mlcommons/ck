from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if 'CM_DOCKER_RUN_SCRIPT_TAGS' not in env:
        env['CM_DOCKER_RUN_SCRIPT_TAGS'] = "run,docker,container"
        CM_RUN_CMD="cm version"
    else:
        CM_RUN_CMD="cm run script --quiet --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS']

    docker_image_base = env.get('CM_DOCKER_IMAGE_BASE', "ubuntu:22.04")
    docker_image_repo = env.get('CM_DOCKER_IMAGE_REPO', "local/" + env['CM_DOCKER_RUN_SCRIPT_TAGS'].replace(',', '-').replace('_',''))
    docker_image_tag = env.get('CM_DOCKER_IMAGE_TAG', docker_image_base.replace(':','-').replace('_','') + "-latest")

    r = cm.access({'action':'search', 'automation':'script', 'tags': env['CM_DOCKER_RUN_SCRIPT_TAGS']})
    if len(r['list']) < 1:
        raise Exception('CM script with tags '+ env['CM_DOCKER_RUN_SCRIPT_TAGS'] + ' not found!')
    PATH = r['list'][0].path
    os.chdir(PATH)
    env['CM_DOCKER_RUN_CMD'] = CM_RUN_CMD
    DOCKER_CONTAINER = docker_image_repo +  ":" + docker_image_tag

    CMD = "docker images -q " +  DOCKER_CONTAINER + " 2> /dev/null"
    docker_image = subprocess.check_output(CMD, shell=True).decode("utf-8")
    recreate_image = env.get('CM_DOCKER_IMAGE_RECREATE', '')

    if docker_image and recreate_image != "yes":
        print("Docker image exists with ID: " + docker_image)
        env['CM_DOCKER_IMAGE_EXISTS'] = "yes"
    elif recreate_image == "yes":
        env['CM_DOCKER_IMAGE_RECREATE'] = "no"

    return {'return':0}

def postprocess(i):

    env = i['env']

    docker_image_base = env.get('CM_DOCKER_IMAGE_BASE', "ubuntu:22.04")
    docker_image_repo = env.get('CM_DOCKER_IMAGE_REPO', "local/" + env['CM_DOCKER_RUN_SCRIPT_TAGS'].replace(',', '-').replace('_',''))
    docker_image_tag = env.get('CM_DOCKER_IMAGE_TAG', docker_image_base.replace(':','-').replace('_','') + "-latest")
    run_cmds = []
    mount_cmds = []
    port_map_cmds = []
    run_opts = ''

    if 'CM_DOCKER_PRE_RUN_COMMANDS' in env:
        for pre_run_cmd in env['CM_DOCKER_PRE_RUN_COMMANDS']:
            run_cmds.append(pre_run_cmd)

    if 'CM_DOCKER_VOLUME_MOUNTS' in env:
        for mounts in env['CM_DOCKER_VOLUME_MOUNTS']:
            mount_cmds.append(mounts)

    if 'CM_DOCKER_PASS_USER_GROUP' in env:
        run_opts += " --group-add $(id -g $USER) "

    if 'CM_DOCKER_ADD_DEVICE' in env:
        run_opts += " --device="+env['CM_DOCKER_ADD_DEVICE']

    if 'CM_DOCKER_PORT_MAPS' in env:
        for ports in env['CM_DOCKER_PORT_MAPS']:
            port_map_cmds.append(ports)

    run_cmd = env['CM_DOCKER_RUN_CMD'] + " " +env.get('CM_DOCKER_RUN_CMD_EXTRA', '').replace(":","=")
    run_cmds.append(run_cmd)
    if 'CM_DOCKER_POST_RUN_COMMANDS' in env:
        for post_run_cmd in env['CM_DOCKER_POST_RUN_COMMANDS']:
            run_cmds.append(post_run_cmd)

    run_cmd = " && ".join(run_cmds)

    if mount_cmds:
        for mount_cmd in mount_cmds:
            mount_parts = mount_cmd.split(":")
            if len(mount_parts) != 2:
                return {'return': 1, 'error': 'Invalid mount {} specified'.format(mount_parts)}
            host_mount = mount_parts[0]
            if not os.path.exists(host_mount):
                os.makedirs(host_mount)

        mount_cmd_string = " -v " + " -v ".join(mount_cmds)
    else:
        mount_cmd_string = ''
    run_opts += mount_cmd_string

    if port_map_cmds:
        port_map_cmd_string = " -p " + "-p ".join(port_map_cmds)
    else:
        port_map_cmd_string = ''
    run_opts += port_map_cmd_string

    if env.get('CM_DOCKER_DETACHED_MODE','') == "yes":
        CONTAINER="docker run -dt "+ run_opts + " --rm " + docker_image_repo + ":" + docker_image_tag + " bash"
        CMD = "ID=`" + CONTAINER + "` && docker exec $ID bash -c '" + run_cmd + "' && docker kill $ID >/dev/null"
        print("Container launch command: " + CMD)
        print("Running "+run_cmd+" inside docker container")
        docker_out = subprocess.check_output(CMD, shell=True).decode("utf-8")
        print(docker_out)
    else:
        CONTAINER="docker run -it --entrypoint '' "+ run_opts + " " + docker_image_repo + ":" + docker_image_tag
        CMD =  CONTAINER + " bash -c '" + run_cmd + " && bash '"
        print("Container launch command: " + CMD)
        docker_out = os.system(CMD)

    return {'return':0}
