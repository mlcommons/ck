from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    dockerfile_path = env.get('CM_DOCKERFILE_WITH_PATH', '')
    if dockerfile_path!='' and os.path.exists(dockerfile_path):
        build_dockerfile = False
        env['CM_BUILD_DOCKERFILE'] = "no"
        os.chdir(os.path.dirname(dockerfile_path))
    else:
        build_dockerfile = True
        env['CM_BUILD_DOCKERFILE'] = "yes"


    CM_DOCKER_BUILD_ARGS = env.get('+ CM_DOCKER_BUILD_ARGS', [])

    if 'CM_GH_TOKEN' in env:
        CM_DOCKER_BUILD_ARGS.append( "CM_GH_TOKEN="+env['CM_GH_TOKEN'] )

    if CM_DOCKER_BUILD_ARGS:
        build_args = "--build-arg "+ " --build-arg ".join(CM_DOCKER_BUILD_ARGS)
    else:
        build_args = ""

    env['CM_DOCKER_BUILD_ARGS'] = build_args

#    if 'CM_DOCKERFILE_WITH_PATH' not in env or not exists(env['CM_DOCKERFILE_WITH_PATH']):
#        env['CM_BUILD_DOCKERFILE'] = "yes"
#    else:
#        env['CM_BUILD_DOCKERFILE'] = "no"
#
    if "CM_DOCKER_IMAGE_REPO" not in env:
        env['CM_DOCKER_IMAGE_REPO'] = "local"

    docker_image_name = env.get('CM_DOCKER_IMAGE_NAME', '')
    if docker_image_name == '':
        docker_image_name = env.get('CM_DOCKER_RUN_SCRIPT_TAGS','').replace(',', '-').replace('_','')
    if docker_image_name == '':
        docker_image_name = 'cm'

    env['CM_DOCKER_IMAGE_NAME'] = docker_image_name

    if env.get("CM_DOCKER_IMAGE_TAG", "") == '':
        env['CM_DOCKER_IMAGE_TAG'] = "latest"

    if env.get("CM_DOCKER_CACHE", "yes") == "no":
        env["CM_DOCKER_CACHE_ARG"] = " --no-cache"

    CMD = ''
    if not build_dockerfile:
        # Write .dockerignore
        with open('.dockerignore', 'w') as f:
            f.write('.git\n')

        # Prepare CMD to build image
        XCMD = [
               'docker build ' + env.get('CM_DOCKER_CACHE_ARG',''),
                ' ' + build_args,
                ' -f "' + dockerfile_path + '"',
                ' -t "' + env.get('CM_DOCKER_IMAGE_REPO', '') + '/' + \
                env.get('CM_DOCKER_IMAGE_NAME', '') + ':' + \
                env.get('CM_DOCKER_IMAGE_TAG', '') + '"',
                ' .'
               ]

        with open(dockerfile_path + '.build.sh', 'w') as f:
            f.write(' \\\n'.join(XCMD) + '\n')

        with open(dockerfile_path + '.build.bat', 'w') as f:
            f.write(' ^\n'.join(XCMD) + '\n')

        CMD = ''.join(XCMD)

        print ('')
        print ('CM generated the following Docker build command:')
        print ('')
        print (CMD)

        print ('')

    env['CM_DOCKER_BUILD_CMD'] = CMD

    return {'return':0}
