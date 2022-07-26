from cmind import utils
import os
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes":
        env['CM_DOCKERFILE_WITH_PATH'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), env['CM_DOCKERFILE_NAME'])

    return {'return':0}
