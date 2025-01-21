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
from os.path import exists


def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    dockerfile_path = env.get('CM_DOCKERFILE_WITH_PATH', '')
    if dockerfile_path != '' and os.path.exists(dockerfile_path):
        build_dockerfile = False
        env['CM_BUILD_DOCKERFILE'] = "no"
        os.chdir(os.path.dirname(dockerfile_path))
    else:
        build_dockerfile = True
        env['CM_BUILD_DOCKERFILE'] = "yes"
        env['CM_DOCKERFILE_BUILD_FROM_IMAGE_SCRIPT'] = "yes"

    CM_DOCKER_BUILD_ARGS = env.get('+ CM_DOCKER_BUILD_ARGS', [])

    if env.get('CM_GH_TOKEN', '') != '':
        CM_DOCKER_BUILD_ARGS.append("CM_GH_TOKEN=" + env['CM_GH_TOKEN'])

    if CM_DOCKER_BUILD_ARGS:
        build_args = "--build-arg " + \
            " --build-arg ".join(CM_DOCKER_BUILD_ARGS)
    else:
        build_args = ""

    env['CM_DOCKER_BUILD_ARGS'] = build_args

#    if 'CM_DOCKERFILE_WITH_PATH' not in env or not exists(env['CM_DOCKERFILE_WITH_PATH']):
#        env['CM_BUILD_DOCKERFILE'] = "yes"
#    else:
#        env['CM_BUILD_DOCKERFILE'] = "no"
#
    if env.get("CM_DOCKER_IMAGE_REPO", "") == '':
        env['CM_DOCKER_IMAGE_REPO'] = "local"

    docker_image_name = env.get('CM_DOCKER_IMAGE_NAME', '')
    if docker_image_name == '':
        docker_image_name = "cm-script-" + \
            env.get('CM_DOCKER_RUN_SCRIPT_TAGS', '').replace(
                ',', '-').replace('_', '-')
        env['CM_DOCKER_IMAGE_NAME'] = docker_image_name

    if env.get("CM_DOCKER_IMAGE_TAG", "") == '':
        env['CM_DOCKER_IMAGE_TAG'] = "latest"

    if str(env.get("CM_DOCKER_CACHE", "yes")).lower() in ["no", "false", "0"]:
        env["CM_DOCKER_CACHE_ARG"] = " --no-cache"

    CMD = ''

    image_name = get_image_name(env)

    if build_dockerfile:
        dockerfile_path = r"\${CM_DOCKERFILE_WITH_PATH}"

    # Write .dockerignore
    with open('.dockerignore', 'w') as f:
        f.write('.git\n')

    # Prepare CMD to build image
    XCMD = [
        'docker build ' + env.get('CM_DOCKER_CACHE_ARG', ''),
        ' ' + build_args,
        ' -f "' + dockerfile_path + '"',
        ' -t "' + image_name,
        ' .'
    ]

    with open(dockerfile_path + '.build.sh', 'w') as f:
        f.write(' \\\n'.join(XCMD) + '\n')

    with open(dockerfile_path + '.build.bat', 'w') as f:
        f.write(' ^\n'.join(XCMD) + '\n')

    CMD = ''.join(XCMD)

    print('================================================')
    print('CM generated the following Docker build command:')
    print('')
    print(CMD)

    print('')

    env['CM_DOCKER_BUILD_CMD'] = CMD

    return {'return': 0}


def get_image_name(env):

    image_name = env.get('CM_DOCKER_IMAGE_REPO', '') + '/' + \
        env.get('CM_DOCKER_IMAGE_NAME', '') + ':' + \
        env.get('CM_DOCKER_IMAGE_TAG', '') + '"'

    return image_name


def postprocess(i):

    env = i['env']

    # Check if need to push docker image to the Docker Hub
    if env.get('CM_DOCKER_PUSH_IMAGE', '') in ['True', True, 'yes']:
        image_name = get_image_name(env)

        # Prepare CMD to build image
        PCMD = 'docker image push ' + image_name

        dockerfile_path = env.get('CM_DOCKERFILE_WITH_PATH', '')
        if dockerfile_path != '' and os.path.isfile(dockerfile_path):
            with open(dockerfile_path + '.push.sh', 'w') as f:
                f.write(PCMD + '\n')

            with open(dockerfile_path + '.build.bat', 'w') as f:
                f.write(PCMD + '\n')

        print('================================================')
        print('CM generated the following Docker push command:')
        print('')
        print(PCMD)

        print('')

        r = os.system(PCMD)
        print('')

        if r > 0:
            return {'return': 1, 'error': 'pushing to Docker Hub failed'}

    return {'return': 0}
