from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    
    if env.get("CM_MODEL_HUGG_PATH","") == "":
        return {'return': 1, 'error': 'CM_MODEL_HUGG_PATH is not set'}
    
    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    return {'return':0}
