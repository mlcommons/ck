from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    script_path = i['run_script_input']['path']

    path = env.get('CM_DOWNLOAD_PATH', '')
    if path == '':
        path = os.getcwd()

    if env.get('CM_GIT_CLONE_REPO', '') != 'yes':
        run_cmd = env.get('CM_PYTHON_BIN_WITH_PATH') + " " +  os.path.join(script_path, 'download_model.py')
    else:
        run_cmd = ''

    env['CM_RUN_CMD'] = run_cmd

    return {'return':0}

def postprocess(i):

    env = i['env']

    env_key = env.get('CM_MODEL_ZOO_ENV_KEY', '')

    path_file = env.get('CM_ML_MODEL_FILE_WITH_PATH','')
    if path_file!='':
        path_dir = os.path.dirname(path_file)

        env['CM_ML_MODEL_PATH'] = path_dir

        if env_key!='':
            env['CM_ML_MODEL_'+env_key+'_PATH'] = path_dir

    else:
        path_dir = env['CM_ML_MODEL_PATH']

    if env_key!='':
        env['CM_ML_MODEL_'+env_key+'_FILE_WITH_PATH'] = path_dir

    return {'return':0}
