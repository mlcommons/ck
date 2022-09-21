from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
