from cmind import utils
import cmind as cm
import os
import json

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if env["CM_DOCKER_OS"] not in [ "ubuntu", "rhel", "arch" ]:
        return {'return': 1, 'error': "Currently only ubuntu, rhel and arch are supported in CM docker"}
    path = i['run_script_input']['path']

    with open(os.path.join(path, "dockerinfo.json")) as f:
        config = json.load(f)

    build_args = []
    input_args = []
    copy_files = []

    if 'CM_DOCKER_RUN_SCRIPT_TAGS' in env:
        script_tags=env['CM_DOCKER_RUN_SCRIPT_TAGS']
        found_scripts = cm.access({'action': 'search', 'automation': 'script', 'tags': script_tags})
        scripts_list = found_scripts['list']

        if not scripts_list:
            return {'return': 1, 'error': 'No CM script found for tags ' + script_tags}

        if len(scripts_list) > 1:
            return {'return': 1, 'error': 'More than one scripts found for tags '+ script_tags}

        script = scripts_list[0]
        input_mapping = script.meta.get('input_mapping', {})
        default_env = script.meta.get('default_env', {})

        for input_,env_ in input_mapping.items():
            if input_ == "docker":
                continue
            arg=env_
            if env_ in default_env: #other inputs to be done later
                arg=arg+"="+default_env[env_]
                #build_args.append(arg)
                #input_args.append("--"+input_+"="+"$"+env_)
 
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
    dockerfile_with_path = env['CM_DOCKERFILE_WITH_PATH']
    dockerfile_dir = os.path.dirname(dockerfile_with_path)

    extra_dir = os.path.dirname(dockerfile_with_path)
    
    if extra_dir!='':
        os.makedirs(extra_dir, exist_ok=True)

    f = open(dockerfile_with_path, "w")
    EOL = env['CM_DOCKER_IMAGE_EOL']
    f.write('FROM ' + docker_image_base + EOL)

    # Maintainers
    f.write(EOL)
    f.write('# Maintained by the MLCommons taskforce on automation and reproducibility' + EOL)
    f.write('LABEL github="https://github.com/mlcommons/ck"' + EOL)
    f.write('LABEL maintainer="https://cKnowledge.org/mlcommons-taskforce"' + EOL)
    f.write(EOL)

    image_label = get_value(env, config, 'LABEL', 'CM_DOCKER_IMAGE_LABEL')
    if image_label:
        f.write('LABEL ' + image_label + EOL)

    shell = get_value(env, config, 'SHELL', 'CM_DOCKER_IMAGE_SHELL')
    if shell:
        f.write('SHELL ' + shell + EOL)

    for arg in config['ARGS']:
        f.write('ARG '+ arg + EOL)

    for build_arg in build_args:
        f.write('ARG '+ build_arg + EOL)

    copy_cmds = []
    if 'CM_DOCKER_COPY_FILES' in env:
        import shutil
        for copy_file in env['CM_DOCKER_COPY_FILES']:
            copy_split = copy_file.split(":")
            if len(copy_split) != 2:
                return {'return': 1, 'error': 'Invalid docker copy input {} given'.format(copy_file)}
            filename = os.path.basename(copy_split[0])
            if not os.path.exists(os.path.join(dockerfile_dir, filename)):
                shutil.copytree(copy_split[0], os.path.join(dockerfile_dir, filename))
            f.write('COPY '+ filename+" "+copy_split[1] + EOL)

    f.write(EOL+'# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes'+EOL+'# Install system dependencies' + EOL)
    f.write('RUN ' + get_value(env, config, 'package-manager-update-cmd', 'CM_PACKAGE_MANAGER_UPDATE_CMD') + EOL)
    f.write('RUN '+ get_value(env, config, 'package-manager-get-cmd') + " " + " ".join(get_value(env, config,
        'packages')) + EOL)

    pip_extra_flags = env.get('CM_DOCKER_PIP_INSTALL_EXTRA_FLAGS', '')

    f.write(EOL+'# Install python packages' + EOL)
    f.write('RUN python3 -m pip install ' + " ".join(get_value(env, config, 'python-packages')) + ' ' + pip_extra_flags + ' ' + EOL)

    f.write(EOL+'# Setup docker environment' + EOL)

    entry_point = get_value(env, config, 'ENTRYPOINT', 'CM_DOCKER_IMAGE_ENTRYPOINT')
    if entry_point:
        f.write('ENTRYPOINT ' + entry_point + EOL)

    for key,value in config['ENV'].items():
        f.write('ENV '+ key + "=\"" + value + "\""+ EOL)
    for cmd in config['RUN_CMDS']:
        f.write('RUN '+ cmd + EOL)

    f.write(EOL+'# Setup docker user' + EOL)
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

    dockerfile_env = i['input'].get('dockerfile_env', {})
    dockerfile_env_input_string = ""
    for docker_env_key in dockerfile_env:
        dockerfile_env_input_string = dockerfile_env_input_string + " --env."+docker_env_key+"="+str(dockerfile_env[docker_env_key])

    workdir = get_value(env, config, 'WORKDIR', 'CM_DOCKER_WORKDIR')
    if workdir:
        f.write('WORKDIR ' + workdir + EOL)
    f.write(EOL+'# Download CM repo for scripts' + EOL)
    f.write('RUN cm pull repo ' + cm_mlops_repo + EOL)

    f.write(EOL+'# Install all system dependencies' + EOL)
    f.write('RUN cm run script --quiet --tags=get,sys-utils-cm' + EOL)

    if 'CM_DOCKER_PRE_RUN_COMMANDS' in env:
        for pre_run_cmd in env['CM_DOCKER_PRE_RUN_COMMANDS']:
            f.write('RUN '+ pre_run_cmd + EOL)

    run_cmd_extra=" "+env.get('CM_DOCKER_RUN_CMD_EXTRA', '').replace(":","=")
    gh_token = get_value(env, config, "GH_TOKEN", "CM_GH_TOKEN")
    if gh_token:
        run_cmd_extra = " --env.CM_GH_TOKEN=$CM_GH_TOKEN"


    f.write(EOL+'# Run commands' + EOL)
    for comment in env.get('CM_DOCKER_RUN_COMMENTS', []):
        f.write(comment + EOL)

    skip_extra = False
    if 'CM_DOCKER_RUN_CMD' not in env:
        if 'CM_DOCKER_RUN_SCRIPT_TAGS' not in env:
            env['CM_DOCKER_RUN_CMD']="cm version"
            skip_extra = True
        else:
            env['CM_DOCKER_RUN_CMD']="cm run script --quiet --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS']

    fake_run = " --fake_run" + dockerfile_env_input_string
    fake_run = fake_run + " --fake_deps" if env.get('CM_DOCKER_FAKE_DEPS') else fake_run

    x = 'RUN ' + env['CM_DOCKER_RUN_CMD']

    if not skip_extra:
        x += fake_run + ' --quiet ' + run_cmd_extra

    f.write(x + EOL)

    #fake_run to install the dependent scripts and caching them
    if not "run" in env['CM_DOCKER_RUN_CMD'] and env.get('CM_REAL_RUN', None):
        fake_run = dockerfile_env_input_string
        f.write('RUN ' + env['CM_DOCKER_RUN_CMD'] + fake_run + run_cmd_extra + ' --quiet ' + EOL)

    if 'CM_DOCKER_POST_RUN_COMMANDS' in env:
        for post_run_cmd in env['CM_DOCKER_POST_RUN_COMMANDS']:
            f.write('RUN '+ post_run_cmd + EOL)

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
