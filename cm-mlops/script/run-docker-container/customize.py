from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']

    env = i['env']


    interactive = env.get('CM_DOCKER_INTERACTIVE_MODE','')

    if interactive:
        env['CM_DOCKER_DETACHED_MODE']='no'

    if 'CM_DOCKER_RUN_SCRIPT_TAGS' not in env:
        env['CM_DOCKER_RUN_SCRIPT_TAGS'] = "run,docker,container"
        CM_RUN_CMD="cm version"
    else:
        CM_RUN_CMD="cm run script --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS'] + ' --quiet'

    # Updating Docker info
    update_docker_info(env)

    docker_image_repo = env['CM_DOCKER_IMAGE_REPO']
    docker_image_base = env['CM_DOCKER_IMAGE_BASE']
    docker_image_name = env['CM_DOCKER_IMAGE_NAME']
    docker_image_tag = env['CM_DOCKER_IMAGE_TAG']

    r = cm.access({'action':'search', 
                   'automation':'script', 
                   'tags': env['CM_DOCKER_RUN_SCRIPT_TAGS']})
    if len(r['list']) < 1:
        raise Exception('CM script with tags '+ env['CM_DOCKER_RUN_SCRIPT_TAGS'] + ' not found!')

    PATH = r['list'][0].path
    os.chdir(PATH)

    env['CM_DOCKER_RUN_CMD'] = CM_RUN_CMD

    DOCKER_CONTAINER = docker_image_repo + "/" + docker_image_name + ":" + docker_image_tag

    CMD = "docker images -q " +  DOCKER_CONTAINER

    if os_info['platform'] == 'windows':
        CMD += " 2> nul"
    else:
        CMD += " 2> /dev/null"

    print ('')
    print ('Checking Docker images:')
    print (CMD)
    print ('')
    
    try:
        docker_image = subprocess.check_output(CMD, shell=True).decode("utf-8")
    except Exception as e:
        return {'return':1, 'error':'Docker is either not installed or not started:\n{}'.format(e)}

    recreate_image = env.get('CM_DOCKER_IMAGE_RECREATE', '')

    if docker_image and recreate_image != "yes":
        print("Docker image exists with ID: " + docker_image)
        env['CM_DOCKER_IMAGE_EXISTS'] = "yes"

    elif recreate_image == "yes":
        env['CM_DOCKER_IMAGE_RECREATE'] = "no"

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']


    # Updating Docker info
    update_docker_info(env)

    docker_image_repo = env['CM_DOCKER_IMAGE_REPO']
    docker_image_base = env['CM_DOCKER_IMAGE_BASE']
    docker_image_name = env['CM_DOCKER_IMAGE_NAME']
    docker_image_tag = env['CM_DOCKER_IMAGE_TAG']

    run_cmds = []
    mount_cmds = []
    port_map_cmds = []
    run_opts = ''

    if env.get('CM_DOCKER_PRE_RUN_COMMANDS', []):
        for pre_run_cmd in env['CM_DOCKER_PRE_RUN_COMMANDS']:
            run_cmds.append(pre_run_cmd)

    if env.get('CM_DOCKER_VOLUME_MOUNTS', []):
        for mounts in env['CM_DOCKER_VOLUME_MOUNTS']:
            mount_cmds.append(mounts)

    if env.get('CM_DOCKER_PASS_USER_GROUP', '') != '':
        run_opts += " --group-add $(id -g $USER) "

    if env.get('CM_DOCKER_ADD_DEVICE', '') != '':
        run_opts += " --device="+env['CM_DOCKER_ADD_DEVICE']

    if env.get('CM_DOCKER_ADD_ALL_GPUS', '') != '':
        run_opts += " --gpus=all"

    if env.get('CM_DOCKER_SHM_SIZE', '') != '':
        run_opts += " --shm-size={}".format(env['CM_DOCKER_SHM_SIZE'])

    if env.get('CM_DOCKER_EXTRA_RUN_ARGS', '') != '':
        run_opts += env['CM_DOCKER_EXTRA_RUN_ARGS']

    if env.get('CM_DOCKER_PORT_MAPS', []):
        for ports in env['CM_DOCKER_PORT_MAPS']:
            port_map_cmds.append(ports)

    run_cmd = env['CM_DOCKER_RUN_CMD'] + " " +env.get('CM_DOCKER_RUN_CMD_EXTRA', '').replace(":","=")
    run_cmds.append(run_cmd)
    if 'CM_DOCKER_POST_RUN_COMMANDS' in env:
        for post_run_cmd in env['CM_DOCKER_POST_RUN_COMMANDS']:
            run_cmds.append(post_run_cmd)

    run_cmd = " && ".join(run_cmds)
    run_cmd = run_cmd.replace("--docker_run_deps", "")

    if mount_cmds:
        for mount_cmd in mount_cmds:

            # Since windows may have 2 :, we search from the right
            j = mount_cmd.rfind(':')
            if j>0:
                mount_parts = [mount_cmd[:j], mount_cmd[j+1:]]
            else:
                return {'return':1, 'error': 'Can\'t find separator : in a mount string: {}'.format(mount_cmd)}
            
#            mount_parts = mount_cmd.split(":")
#            if len(mount_parts) != 2:
#                return {'return': 1, 'error': 'Invalid mount {} specified'.format(mount_parts)}

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

    # Currently have problem running Docker in detached mode on Windows:
    detached = env.get('CM_DOCKER_DETACHED_MODE','') in ['yes', 'True', True]
#    if detached and os_info['platform'] != 'windows':
    if detached:
        if os_info['platform'] == 'windows':
            return {'return':1, 'error':'Currently we don\'t support running Docker containers in detached mode on Windows - TBD'}

        CONTAINER="docker run -dt "+ run_opts + " --rm " + docker_image_repo + "/" + docker_image_name + ":" + docker_image_tag + " bash"
        CMD = "ID=`" + CONTAINER + "` && docker exec $ID bash -c '" + run_cmd + "' && docker kill $ID >/dev/null"

        print ('')
        print ("Container launch command:")
        print ('')
        print (CMD)
        print ('')
        print ("Running "+run_cmd+" inside docker container")

        record_script({'cmd':CMD, 'env': env})

        print ('')
        docker_out = subprocess.check_output(CMD, shell=True).decode("utf-8")

        print(docker_out)

    else:
        x = "'"
        if os_info['platform'] == 'windows':
            x = '"'

        x1 = ''
        x2 = ''
        if env.get('CM_DOCKER_INTERACTIVE_MODE', '') in ['yes', 'True', True]:
            x1 = '-it'
            x2 = " && bash "


        CONTAINER="docker run " + x1 + " --entrypoint " + x + x + " " + run_opts + " " + docker_image_repo + "/" + docker_image_name + ":" + docker_image_tag
        CMD =  CONTAINER + " bash -c " + x + run_cmd + x2 + x

        print ('')
        print ("Container launch command:")
        print ('')
        print (CMD)

        record_script({'cmd':CMD, 'env': env})

        print ('')
        docker_out = os.system(CMD)

    return {'return':0}

def record_script(i):

    cmd = i['cmd']
    env = i['env']

    files = []

    dockerfile_path = env.get('CM_DOCKERFILE_WITH_PATH', '')
    if dockerfile_path != '' and os.path.isfile(dockerfile_path):
        files.append(dockerfile_path + '.run.bat')
        files.append(dockerfile_path + '.run.sh')

    save_script = env.get('CM_DOCKER_SAVE_SCRIPT', '')
    if save_script != '':
        if save_script.endswith('.bat') or save_script.endswith('.sh'):
            files.append(save_script)
        else:
            files.append(save_script+'.bat')
            files.append(save_script+'.sh')

    for filename in files:
        with open (filename, 'w') as f:
            f.write(cmd + '\n')

    return {'return':0}

def update_docker_info(env):
    # Updating Docker info
    docker_image_repo = env.get('CM_DOCKER_IMAGE_REPO', 'cknowledge')
    env['CM_DOCKER_IMAGE_REPO'] = docker_image_repo

    docker_image_base = env.get('CM_DOCKER_IMAGE_BASE')
    if not docker_image_base:
        if env.get("CM_DOCKER_OS", '') != '':
            docker_image_base = env["CM_DOCKER_OS"]+":"+env["CM_DOCKER_OS_VERSION"]
        else:
            docker_image_base = "ubuntu:22.04"
    env['CM_DOCKER_IMAGE_BASE'] = docker_image_base

    docker_image_name = env.get('CM_DOCKER_IMAGE_NAME', 'cm-script-'+env['CM_DOCKER_RUN_SCRIPT_TAGS'].replace(',', '-').replace('_',''))
    env['CM_DOCKER_IMAGE_NAME'] = docker_image_name

    docker_image_tag = env.get('CM_DOCKER_IMAGE_TAG', docker_image_base.replace(':','-').replace('_','') + "-latest")
    env['CM_DOCKER_IMAGE_TAG'] = docker_image_tag

    return
