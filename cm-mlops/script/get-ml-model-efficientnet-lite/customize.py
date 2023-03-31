from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']
    env['CM_ML_MODEL_STARTING_WEIGHTS_FILENAME'] = url

    print ('Downloading from {}'.format(url))

    r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':url})
    if r['return']>0: return r

    filename = r['filename']

    if env.get('CM_UNZIP') == "yes" or env.get('CM_UNTAR') == "yes":
        if env.get('CM_UNZIP') == "yes":
            cmd="unzip "
        elif env.get('CM_UNTAR') == "yes":
            cmd="tar -xvzf "
        os.system(cmd+filename)

        filename = env['CM_ML_MODEL_FILE']

        extract_folder = env.get('CM_EXTRACT_FOLDER', '')

        if extract_folder:
            env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, extract_folder, filename)
        else:
            env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, filename)
    else:
        env['CM_ML_MODEL_FILE']=filename
        env['CM_ML_MODEL_FILE_WITH_PATH']=r['path']

    env['CM_ML_MODEL_PATH']=path

    if not os.path.exists(env['CM_ML_MODEL_FILE_WITH_PATH']):
        return {'return':1, 'error': f"Model file path {env['CM_ML_MODEL_FILE_WITH_PATH']} not existing. Probably the model name {env['CM_ML_MODEL_FILE']} in model meta is wrong"}

    return {'return':0}
