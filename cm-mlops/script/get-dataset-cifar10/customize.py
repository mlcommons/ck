from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    return {'return': 0}

def postprocess(i):
    env = i['env']

    variation_tags = i.get('variation_tags',[])

    return {'return': 0}
