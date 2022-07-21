from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    CM_RUN_CMD="cm run script --tags=" + env['CM_DOCKER_RUN_SCRIPT_TAGS']

    if env['CM_RUN_DOCKER'] == "yes":

        env['CM_DOCKER_IMAGE_RUN_CMD']=CM_RUN_CMD
        env['CM_DOCKER_IMAGE_REPO'] = "local/image_classification_onnx_py"
        env['CM_DOCKER_IMAGE_TAG'] = "latest"
        CMD = "docker images -q " +  env['CM_DOCKER_IMAGE_REPO'] + ":" + env['CM_DOCKER_IMAGE_TAG'] + " 2> /dev/null >docker_exists"
        f = open("docker_exists", "r")
        docker_image = f.read()
        if docker_image:
            print("Docker image exists with ID: " + docker_image)
            DOCKER_RUN_CMD="docker exec " + docker_image + " bash -c '" + CM_RUN_CMD + "'"
            print("Running docker CMD: " +DOCKER_RUN_CMD)
            os.system(DOCKER_RUN_CMD)
            env['CM_DOCKER_IMAGE_EXISTS'] = "yes"
        else:
            env['CM_DOCKERFILE_WITH_PATH'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                env['CM_DOCKERFILE_NAME'])
            env['CM_RUN_DOCKERFILE'] = "yes"
            env['CM_DOCKER_IMAGE_REPO'] = "local/image_classification_onnx_py"
            env['CM_DOCKER_IMAGE_TAG'] = "latest"

    return {'return':0}
