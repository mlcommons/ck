from cmind import utils
import os

def preprocess(i):

    env = i['env']
    path = i['run_script_input']['path']
    env['+PYTHONPATH'] =  [ os.path.join(path, "src") ]

    return {'return': 0}
