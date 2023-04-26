from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    
    env = i['env']
    url = env['CM_WGET_URL']
    filename=os.path.basename(url)
    env['CM_WGET_ZIP_FILE_NAME'] = filename

    return {'return':0}


def postprocess(i):
    env = i['env']

    env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = os.path.join(os.getcwd(), 'openimages-mlperf.json')
    env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(os.getcwd())
    env['CM_DATASET_OPENIMAGES_ANNOTATIONS_FILE_PATH'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']
    env['CM_DATASET_OPENIMAGES_ANNOTATIONS_DIR_PATH'] = env['CM_DATASET_ANNOTATIONS_DIR_PATH']

    return {'return':0}
