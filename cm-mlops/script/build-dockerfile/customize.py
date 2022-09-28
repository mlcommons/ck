from cmind import utils
import os
import json

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if 'CM_DOCKER_IMAGE_EOL' not in env:
        env['CM_DOCKER_IMAGE_EOL'] = "\n"
    if "CM_DOCKER_OS" not in env:
        env["CM_DOCKER_OS"] = "ubuntu"
    if env["CM_DOCKER_OS"] not in [ "ubuntu", "rhel" ]:
        return {'return': 1, 'error': "Currently only ubuntu and rhel are supported in CM docker"}
    path = i['run_script_input']['path']
    with open(os.path.join(path, "dockerinfo.json")) as f:
        config = json.load(f)

    if "CM_DOCKER_OS_VERSION" not in env:
        env["CM_DOCKER_OS_VERSION"] = "20.04"

    docker_image_base = get_value(env, config, 'FROM', 'CM_DOCKER_IMAGE_BASE')
    if not docker_image_base:
        if env["CM_DOCKER_OS"] == "ubuntu":
            docker_image_base = env["CM_DOCKER_OS"]+":"+env["CM_DOCKER_OS_VERSION"]
        else:
            return {'return': 1, 'error': "Version "+env["CM_DOCKER_OS_VERSION"]+" is not supported yet"}

    if "CM_MLOPS_REPO" in env:
        cm_mlops_repo = env["CM_MLOPS_REPO"]
    else:
        cm_mlops_repo = "mlcommons@ck"

    if 'CM_DOCKERFILE_WITH_PATH' not in env:
        env['CM_DOCKERFILE_WITH_PATH'] = os.path.join(os.getcwd(), "Dockerfile")
    if 'CM_DOCKER_IMAGE_RUN_CMD' not in env:
        env['CM_DOCKER_IMAGE_RUN_CMD'] = "cm version"
    f = open(env['CM_DOCKERFILE_WITH_PATH'], "w")
    EOL = env['CM_DOCKER_IMAGE_EOL']
    f.write('FROM ' + docker_image_base + EOL)
    image_label = get_value(env, config, 'LABEL', 'CM_DOCKER_IMAGE_LABEL')
    if image_label:
        f.write('LABEL ' + image_label + EOL)
    shell = get_value(env, config, 'SHELL', 'CM_DOCKER_IMAGE_SHELL')
    if shell:
        f.write('SHELL ' + shell + EOL)
    f.write('RUN ' + get_value(env, config, 'package-manager-update-cmd') + EOL)
    f.write('RUN '+ get_value(env, config, 'package-manager-get-cmd') + " " + " ".join(get_value(env, config,
        'packages')) + EOL)
    f.write('RUN python3 -m pip install ' + " ".join(get_value(env, config, 'python-packages')) + EOL)
    entry_point = get_value(env, config, 'ENTRYPOINT', 'CM_DOCKER_IMAGE_ENTRYPOINT')
    if entry_point:
        f.write('ENTRYPOINT ' + entry_point + EOL)
    for key,value in config['ENV'].items():
        f.write('ENV '+ key + "=" + value + EOL)
    for cmd in config['RUN_CMDS']:
        f.write('RUN '+ cmd + EOL)
    docker_user = get_value(env, config, 'USER', 'CM_DOCKER_USER')
    docker_userid = get_value(env, config, 'USERID', 'CM_DOCKER_USER_ID')
    docker_group = get_value(env, config, 'GROUP', 'CM_DOCKER_GROUP')
    docker_groupid = get_value(env, config, 'GROUPID', 'CM_DOCKER_GROUP_ID')
    if docker_user:
        if not docker_group:
            docker_group = docker_user
        DOCKER_GROUP = ' -g ' + docker_group
        if docker_groupid:
            DOCKER_GROUP_ID = "-g " + docker_groupid
        else:
            DOCKER_GROUP_ID = ""
        f.write('RUN groupadd ' + DOCKER_GROUP_ID + docker_group + EOL)
        if docker_userid:
            DOCKER_USER_ID = "-u " + docker_userid
        else:
            DOCKER_USER_ID = ""
        user_shell = json.loads(shell)
        f.write('RUN useradd ' + DOCKER_USER_ID  + DOCKER_GROUP + ' --create-home --shell '+ user_shell[0] + ' '
                + docker_user + EOL)
        f.write('RUN echo "' + docker_user + ' ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers' + EOL)
        f.write('USER ' + docker_user + ":" + docker_group + EOL)
    workdir = get_value(env, config, 'WORKDIR', 'CM_DOCKER_WORKDIR')
    if workdir:
        f.write('WORKDIR ' + workdir + EOL)
    f.write('RUN cm pull repo ' + cm_mlops_repo + EOL)
    #echo '${CM_DOCKER_IMAGE_ENV}'

    f.write('RUN cm run script --quiet --tags=get,sys-utils-cm' + EOL)
    if "run" in env['CM_DOCKER_IMAGE_RUN_CMD']:
        fake_run = " --fake_run"
    else:
        fake_run = ""
    f.write('RUN ' + env['CM_DOCKER_IMAGE_RUN_CMD'] + fake_run + EOL)

    f.close()

    f = open(env['CM_DOCKERFILE_WITH_PATH'], "r")
    print(f.read())

    return {'return':0}

def get_value(env, config, key, env_key = None):
    if not env_key:
        env_key = key
    if env_key in env:
        return env[env_key]
    docker_os = env['CM_DOCKER_OS']
    docker_os_version = env['CM_DOCKER_OS_VERSION']
    version_meta = config['distros'][docker_os]['versions'].get(docker_os_version, {})
    if key in version_meta:
        return version_meta[key]
    distro_meta = config['distros'][docker_os]
    if key in distro_meta:
        return distro_meta[key]
    if key in config:
        return config[key]
    return None
