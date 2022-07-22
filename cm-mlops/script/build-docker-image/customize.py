from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if not exists(env['CM_DOCKERFILE_WITH_PATH']):
        env['CM_BUILD_DOCKERFILE'] = "yes"
        env['CM_RUN_DOCKERFILE'] = "yes"
    else:
        env['CM_BUILD_DOCKERFILE'] = "no"
    if "CM_DOCKER_IMAGE_REPO" not in env:
        env['CM_DOCKER_IMAGE_REPO'] = "local"
    if "CM_DOCKER_IMAGE_TAG" not in env:
        env['CM_DOCKER_IMAGE_TAG'] = "latest"

    return {'return':0}
