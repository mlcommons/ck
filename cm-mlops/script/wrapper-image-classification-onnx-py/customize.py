from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    CM_RUN_CMD="cm run script --quiet --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS']

    if env['CM_RUN_DOCKER'] == "yes":

        env['CM_DOCKER_IMAGE_RUN_CMD']=CM_RUN_CMD
        CMD = "docker images -q " +  env['CM_DOCKER_IMAGE_REPO'] + ":" + env['CM_DOCKER_IMAGE_TAG'] + " 2> /dev/null >docker_exists"
        os.system(CMD)
        f = open("docker_exists", "r")
        docker_image = f.read()
        if docker_image:
            print("Docker image exists with ID: " + docker_image)
            CONTAINER="docker run -dt --rm " + env['CM_DOCKER_IMAGE_REPO'] + ":" + env['CM_DOCKER_IMAGE_TAG'] + " bash"
            os.system("ID=`" + CONTAINER + "` && docker exec $ID bash -c '" + env['CM_DOCKER_IMAGE_RUN_CMD'])
            env['CM_DOCKER_IMAGE_EXISTS'] = "yes"
        else:
            env['CM_DOCKERFILE_WITH_PATH'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                env['CM_DOCKERFILE_NAME'])
            env['CM_RUN_DOCKERFILE'] = "yes"
            env['CM_RUN_DOCKER_CONTAINER'] = "yes"

    return {'return':0}
