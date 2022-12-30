from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']

    env['CM_STARTING_WEIGHTS_FILENAME'] = url

    print ('Downloading from {}'.format(url))

    if url.endswith(".gz") or url.endswith(".tflite"):
        env['CM_TMP_WGET'] = "yes"
        if url.endswith(".tflite"):
            env['CM_ML_MODEL_FILE']=os.path.basename(url)
        elif url.endswith(".gz"):
            env['CM_TMP_EXTRACT'] = "yes"
            env['CM_TMP_EXTRACT_FILE_NAME'] = os.path.basename(url)
            env['CM_ML_MODEL_FILE']=env['CM_TMP_EXTRACT_FILE_NAME'][:-3]
        env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(os.getcwd(), env['CM_ML_MODEL_FILE'])
    else:
        r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':url})
        if r['return']>0: return r
        env['CM_ML_MODEL_FILE']=r['filename']
        env['CM_ML_MODEL_FILE_WITH_PATH']=r['path']

    # Add to path
    env['CM_ML_MODEL_PATH']=path

    return {'return':0}
