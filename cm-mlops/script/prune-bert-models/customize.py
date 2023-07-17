from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    print("Entered preprocess")

    return {'return': 0}

def postprocess(i):

    env = i['env']

    print("Entered postprocess")

    return {'return': 0}