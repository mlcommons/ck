from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    run_cmd="python setup.py install"

    env['CM_RUN_CMD'] = run_cmd

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    return {'return':0}
