from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    print ('')
    print ('Running preprocess function in customize.py ...')

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']

#    print ('')
#    print ('Running postprocess function in customize.py ...')
    
    return {'return':0}
