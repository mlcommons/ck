from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']

    env = i['env']

    print ('')
    print ('Current directory: {}'.format(os.getcwd()))
    
    print ('')
    for k in ['CM_ABTF_SSD_PYTORCH', 'CM_ML_MODEL_FILE_WITH_PATH']:
        v = env.get(k, '')

        print ('ENV["{}"] = {}'.format(k,v))

    print ('')

    return {'return':0}

def postprocess(i):

    return {'return':0}
