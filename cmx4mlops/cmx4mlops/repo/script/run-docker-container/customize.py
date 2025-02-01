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
import subprocess
from os.path import exists


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    interactive = env.get('CM_DOCKER_INTERACTIVE_MODE', '')

    if str(interactive).lower() in ['yes', 'true', '1']:
        env['CM_DOCKER_DETACHED_MODE'] = 'no'

    if 'CM_DOCKER_RUN_SCRIPT_TAGS' not in env:
        env['CM_DOCKER_RUN_SCRIPT_TAGS'] = "run,docker,container"
        CM_RUN_CMD = "cm version"
    else:
        CM_RUN_CMD = "cm run script --tags=" + \
            env['CM_DOCKER_RUN_SCRIPT_TAGS'] + ' --quiet'

    r = cm.access({'action': 'search',
                   'automation': 'script',
                   'tags': env['CM_DOCKER_RUN_SCRIPT_TAGS']})
    if len(r['list']) < 1:
        raise Exception(
            'CM script with tags ' +
            env['CM_DOCKER_RUN_SCRIPT_TAGS'] +
            ' not found!')

    PATH = r['list'][0].path
    os.chdir(PATH)

    env['CM_DOCKER_RUN_CMD'] = CM_RUN_CMD

    # Updating Docker info
    update_docker_info(env)

    docker_image_repo = env['CM_DOCKER_IMAGE_REPO']
    docker_image_base = env['CM_DOCKER_IMAGE_BASE']
    docker_image_name = env['CM_DOCKER_IMAGE_NAME']
    docker_image_tag = env['CM_DOCKER_IMAGE_TAG']

    DOCKER_CONTAINER = docker_image_repo + "/" + \
        docker_image_name + ":" + docker_image_tag

    print('')
    print('Checking existing Docker container:')
    print('')
    CMD = f"""docker ps --filter "ancestor={DOCKER_CONTAINER}" """
    if os_info['platform'] == 'windows':
        CMD += " 2> nul"
    else:
        CMD += " 2> /dev/null"
    print('  ' + CMD)
    print('')

    try:
        docker_container = subprocess.check_output(
            CMD, shell=True).decode("utf-8")
    except Exception as e:
        return {
            'return': 1, 'error': 'Docker is either not installed or not started:\n{}'.format(e)}

    output_split = docker_container.split("\n")
    if len(output_split) > 1 and str(env.get('CM_DOCKER_REUSE_EXISTING_CONTAINER',
                                             '')).lower() in ["1", "true", "yes"]:  # container exists
        out = output_split[1].split(" ")
        existing_container_id = out[0]
        print(f"Reusing existing container {existing_container_id}")
        env['CM_DOCKER_CONTAINER_ID'] = existing_container_id

    else:
        if env.get('CM_DOCKER_CONTAINER_ID', '') != '':
            del (env['CM_DOCKER_CONTAINER_ID'])  # not valid ID

        CMD = "docker images -q " + DOCKER_CONTAINER

        if os_info['platform'] == 'windows':
            CMD += " 2> nul"
        else:
            CMD += " 2> /dev/null"

        print('')
        print('Checking Docker images:')
        print('')
        print('  ' + CMD)
        print('')

        try:
            docker_image = subprocess.check_output(
                CMD, shell=True).decode("utf-8")
        except Exception as e:
            return {
                'return': 1, 'error': 'Docker is either not installed or not started:\n{}'.format(e)}

        recreate_image = env.get('CM_DOCKER_IMAGE_RECREATE', '')

        if recreate_image != 'yes':
            if docker_image:
                print("Docker image exists with ID: " + docker_image)
                env['CM_DOCKER_IMAGE_EXISTS'] = "yes"

    #    elif recreate_image == "yes":
    #        env['CM_DOCKER_IMAGE_RECREATE'] = "no"

    return {'return': 0}


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

    # not completed as su command breaks the execution sequence
    #
    # if env.get('CM_DOCKER_PASS_USER_ID', '') != '':
    #    run_opts += " --user 0 "
    #    run_cmds.append(f"(usermod -u {os.getuid()} cmuser || echo pass)")
    #    run_cmds.append(f"(chown -R {os.getuid()}:{os.getuid()} /home/cmuser  || echo pass)")
    #    run_cmds.append(" ( su cmuser )")
    #    run_cmds.append('export PATH="/home/cmuser/venv/cm/bin:$PATH"')

    if env.get('CM_DOCKER_PRE_RUN_COMMANDS', []):
        for pre_run_cmd in env['CM_DOCKER_PRE_RUN_COMMANDS']:
            run_cmds.append(pre_run_cmd)

    if env.get('CM_DOCKER_VOLUME_MOUNTS', []):
        for mounts in env['CM_DOCKER_VOLUME_MOUNTS']:
            mount_cmds.append(mounts)

    if env.get('CM_DOCKER_PASS_USER_GROUP', '') != '':
        run_opts += " --group-add $(id -g $USER) "

    if env.get('CM_DOCKER_ADD_DEVICE', '') != '':
        run_opts += " --device=" + env['CM_DOCKER_ADD_DEVICE']

    if env.get('CM_DOCKER_PRIVILEGED_MODE', '') == 'yes':
        run_opts += " --privileged "

    if env.get('CM_DOCKER_ADD_NUM_GPUS', '') != '':
        run_opts += " --gpus={}".format(env['CM_DOCKER_ADD_NUM_GPUS'])
    elif env.get('CM_DOCKER_ADD_ALL_GPUS', '') != '':
        run_opts += " --gpus=all"

    if env.get('CM_DOCKER_SHM_SIZE', '') != '':
        run_opts += " --shm-size={}".format(env['CM_DOCKER_SHM_SIZE'])

    if env.get('CM_DOCKER_EXTRA_RUN_ARGS', '') != '':
        run_opts += env['CM_DOCKER_EXTRA_RUN_ARGS']

    if env.get('CM_DOCKER_PORT_MAPS', []):
        for ports in env['CM_DOCKER_PORT_MAPS']:
            port_map_cmds.append(ports)

    run_cmd = env['CM_DOCKER_RUN_CMD'] + " " + \
        env.get('CM_DOCKER_RUN_CMD_EXTRA', '').replace(":", "=")
    run_cmds.append(run_cmd)
    if 'CM_DOCKER_POST_RUN_COMMANDS' in env:
        for post_run_cmd in env['CM_DOCKER_POST_RUN_COMMANDS']:
            run_cmds.append(post_run_cmd)

    run_cmd = " && ".join(run_cmds)
    run_cmd = run_cmd.replace("--docker_run_deps", "")

    if mount_cmds:
        for i, mount_cmd in enumerate(mount_cmds):

            # Since windows may have 2 :, we search from the right
            j = mount_cmd.rfind(':')
            if j > 0:
                mount_parts = [mount_cmd[:j], mount_cmd[j + 1:]]
            else:
                return {'return': 1, 'error': 'Can\'t find separator : in a mount string: {}'.format(
                    mount_cmd)}

#            mount_parts = mount_cmd.split(":")
#            if len(mount_parts) != 2:
# return {'return': 1, 'error': 'Invalid mount {}
# specified'.format(mount_parts)}

            host_mount = mount_parts[0]

            if not os.path.exists(host_mount):
                os.makedirs(host_mount)

            abs_host_mount = os.path.abspath(mount_parts[0])

            if abs_host_mount != host_mount or " " in abs_host_mount and not host_mount.startswith(
                    '"'):
                mount_cmds[i] = f"\"{abs_host_mount}\":{mount_parts[1]}"

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
    detached = str(
        env.get(
            'CM_DOCKER_DETACHED_MODE',
            '')).lower() in [
        'yes',
        'true',
        "1"]
#    if detached and os_info['platform'] != 'windows':
    if detached:
        if os_info['platform'] == 'windows':
            return {
                'return': 1, 'error': 'Currently we don\'t support running Docker containers in detached mode on Windows - TBD'}

        existing_container_id = env.get('CM_DOCKER_CONTAINER_ID', '')
        if existing_container_id:
            CMD = f"ID={existing_container_id} && docker exec $ID bash -c '" + run_cmd + "'"
        else:
            CONTAINER = f"docker run -dt {run_opts} --rm  {docker_image_repo}/{docker_image_name}:{docker_image_tag} bash"
            CMD = f"ID=`{CONTAINER}` && docker exec $ID bash -c '{run_cmd}'"

            if False and str(env.get('CM_KEEP_DETACHED_CONTAINER', '')).lower() not in [
                    'yes', "1", 'true']:
                CMD += " && docker kill $ID >/dev/null"

        CMD += ' && echo "ID=$ID"'

        print('=========================')
        print("Container launch command:")
        print('')
        print(CMD)
        print('')
        print("Running " + run_cmd + " inside docker container")

        record_script({'cmd': CMD, 'env': env})

        print('')
        # Execute the command
        try:
            result = subprocess.run(
                CMD,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
            print("Command Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error Occurred!")
            print(f"Command: {e.cmd}")
            print(f"Return Code: {e.returncode}")
            print(f"Error Output: {e.stderr}")
            return {'return': 1, 'error': e.stderr}

        docker_out = result.stdout
        # if docker_out != 0:
        #    return {'return': docker_out, 'error': 'docker run failed'}

        lines = docker_out.split("\n")

        for line in lines:
            if line.startswith("ID="):
                ID = line[3:]
                env['CM_DOCKER_CONTAINER_ID'] = ID

        print(docker_out)

    else:
        x = "'"
        if os_info['platform'] == 'windows':
            x = '"'

        x1 = ''
        x2 = ''
        run_cmd_prefix = ""
        if env.get('CM_DOCKER_INTERACTIVE_MODE', '') in ['yes', 'True', True]:
            run_cmd_prefix = "("
            x1 = '-it'
            x2 = " && bash ) || bash"

        CONTAINER = "docker run " + x1 + " --entrypoint " + x + x + " " + run_opts + \
            " " + docker_image_repo + "/" + docker_image_name + ":" + docker_image_tag
        CMD = CONTAINER + " bash -c " + x + run_cmd_prefix + run_cmd + x2 + x

        print('')
        print("Container launch command:")
        print('')
        print(CMD)

        record_script({'cmd': CMD, 'env': env})

        print('')
        docker_out = os.system(CMD)
        if docker_out != 0:
            return {'return': docker_out, 'error': 'docker run failed'}

    return {'return': 0}


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
            files.append(save_script + '.bat')
            files.append(save_script + '.sh')

    for filename in files:
        with open(filename, 'w') as f:
            f.write(cmd + '\n')

    return {'return': 0}


def update_docker_info(env):

    # Updating Docker info
    docker_image_repo = env.get('CM_DOCKER_IMAGE_REPO', 'local')
    env['CM_DOCKER_IMAGE_REPO'] = docker_image_repo

    docker_image_base = env.get('CM_DOCKER_IMAGE_BASE')
    if not docker_image_base:
        if env.get("CM_DOCKER_OS", '') != '':
            docker_image_base = env["CM_DOCKER_OS"] + \
                ":" + env["CM_DOCKER_OS_VERSION"]
        else:
            docker_image_base = "ubuntu:22.04"

    env['CM_DOCKER_IMAGE_BASE'] = docker_image_base

    if env.get('CM_DOCKER_IMAGE_NAME', '') != '':
        docker_image_name = env['CM_DOCKER_IMAGE_NAME']
    else:
        docker_image_name = 'cm-script-' + \
            env['CM_DOCKER_RUN_SCRIPT_TAGS'].replace(
                ',', '-').replace('_', '-').replace('+', 'plus')
        env['CM_DOCKER_IMAGE_NAME'] = docker_image_name

    docker_image_tag_extra = env.get('CM_DOCKER_IMAGE_TAG_EXTRA', '-latest')

    docker_image_tag = env.get('CM_DOCKER_IMAGE_TAG', docker_image_base.replace(
        ':', '-').replace('_', '').replace("/", "-") + docker_image_tag_extra)
    env['CM_DOCKER_IMAGE_TAG'] = docker_image_tag

    return
