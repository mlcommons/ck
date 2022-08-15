from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    CM_RUN_CMD="cm run script --quiet --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS']
    r = cm.access({'action':'search', 'automation':'script', 'tags': env['CM_DOCKER_RUN_SCRIPT_TAGS']})
    if len(r['list']) < 1:
        raise Exception('CM script with tags '+ env['CM_DOCKER_RUN_SCRIPT_TAGS'] + ' not found!')
    PATH = r['list'][0].path
    os.chdir(PATH)
    env['CM_DOCKER_IMAGE_RUN_CMD'] = CM_RUN_CMD
    DOCKER_CONTAINER = env['CM_DOCKER_IMAGE_REPO'] +  ":" + env['CM_DOCKER_IMAGE_TAG'] 

    CMD = "docker images -q " +  DOCKER_CONTAINER + " 2> /dev/null"
    docker_image = subprocess.check_output(CMD, shell=True).decode("utf-8") 

    if docker_image:
        print("Docker image exists with ID: " + docker_image)
        CONTAINER="docker run -dt --rm " + env['CM_DOCKER_IMAGE_REPO'] + ":" + env['CM_DOCKER_IMAGE_TAG'] + " bash"
        os.system("ID=`" + CONTAINER + "` && docker exec $ID bash -c '" + env['CM_DOCKER_IMAGE_RUN_CMD'] + "' && docker kill $ID")
        env['CM_DOCKER_IMAGE_EXISTS'] = "yes"

    return {'return':0}
