from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
