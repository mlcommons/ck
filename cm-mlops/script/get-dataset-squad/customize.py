from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    env = i['env']

    env['CM_DATASET_SQUAD_PATH'] = os.getcwd()
    env['CM_DATASET_PATH'] = os.getcwd()
    env['CM_DATASET_SQUAD_VAL_PATH'] = os.path.join(os.getcwd(), env['CM_VAL_FILENAME'])

    return {'return':0}
