from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    
    f = open(env['CM_DOCKERFILE_WITH_PATH'], "w")
    EOL = env['CM_DOCKER_IMAGE_EOL']
    f.write('FROM ' + env['CM_DOCKER_IMAGE_BASE'] + EOL)
    if 'CM_DOCKER_IMAGE_LABEL' in env and env['CM_DOCKER_IMAGE_LABEL']:
        f.write('LABEL ' + env['CM_DOCKER_IMAGE_LABEL'] + EOL)
    if 'CM_DOCKER_IMAGE_SHELL' in env and env['CM_DOCKER_IMAGE_SHELL']:
        f.write('SHELL ' + env['CM_DOCKER_IMAGE_SHELL'] + EOL)
    f.write('RUN apt update -y' + EOL)
    f.write('RUN apt install -y python3 python3-pip git sudo' + EOL)
    f.write('RUN python3 -m pip install cmind requests' + EOL)
    if 'CM_DOCKER_IMAGE_ENTRYPOINT' in env and env['CM_DOCKER_IMAGE_ENTRYPOINT']:
        f.write('ENTRYPOINT ' + env['CM_DOCKER_IMAGE_ENTRYPOINT'] + EOL)
    if 'CM_DOCKER_IMAGE_TZ' in env:
        f.write('ENV TZ=' + env['CM_DOCKER_IMAGE_TZ'] + EOL)
        f.write('RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone' + EOL)

    if 'CM_DOCKER_USER' in env:
        if 'CM_DOCKER_GROUP' not in env:
            env['CM_DOCKER_GROUP'] = env['CM_DOCKER_USER']
        DOCKER_GROUP = ' -g ' + env['CM_DOCKER_GROUP']
        if 'CM_DOCKER_GROUP_ID' in env:
            DOCKER_GROUP_ID = "-g " + env['CM_DOCKER_GROUP_ID']
        else:
            DOCKER_GROUP_ID = ""
        f.write('RUN groupadd ' + DOCKER_GROUP_ID + env['CM_DOCKER_GROUP'] + EOL)
        if 'CM_DOCKER_USER_ID' in env:
            DOCKER_USER_ID = "-u " + env['CM_DOCKER_USER_ID']
        else:
            DOCKER_USER_ID = ""
        f.write('RUN useradd ' + DOCKER_USER_ID  + DOCKER_GROUP + ' --create-home --shell /bin/bash '
                + env['CM_DOCKER_USER'] + EOL)
        f.write('RUN echo "' + env['CM_DOCKER_USER'] + ' ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers' + EOL)
        f.write('USER ' + env['CM_DOCKER_USER'] + ":" + env['CM_DOCKER_GROUP'] + EOL)
    if 'CM_DOCKER_WORKDIR' in env:
        f.write('WORKDIR ' + env['CM_DOCKER_WORKDIR'] + EOL)
    f.write('RUN cm pull repo mlcommons@ck' + EOL)
    #echo '${CM_DOCKER_IMAGE_ENV}'

    f.write('RUN cm run script --quiet --tags=get,sys-utils-cm' + EOL)

    f.write('RUN ' + env['CM_DOCKER_IMAGE_RUN_CMD'] + EOL)

    f.close()

    f = open(env['CM_DOCKERFILE_WITH_PATH'], "r")
    print(f.read())

    return {'return':0}
