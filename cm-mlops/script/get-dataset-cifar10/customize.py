from cmind import utils
import os

def postprocess(i):
    env = i['env']

    env['CM_DATASET_CIFAR10_PATH'] = os.getcwd()
    env['CM_DATASET_PATH'] = os.getcwd()

    return {'return':0}
