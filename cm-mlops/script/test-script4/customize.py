from cmind import utils
import os

def preprocess(i):

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['+CM_LIST_ENV']=['c']

    return {'return':0}
