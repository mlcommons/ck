from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    print(i)

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'

    return {'return':0}
