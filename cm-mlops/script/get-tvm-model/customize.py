from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')
    
    work_dir = env.get('CM_TUNE_TVM_MODEL_WORKDIR', '')

    if work_dir != '':
        if not os.path.exists(work_dir):
            raise FileNotFoundError(
                f"Error: the specified path \"{work_dir}\"does not exist")

        if not os.path.exists(f"{work_dir}/database_workload.json"):
            raise FileNotFoundError(
                "Error: the found workdir does not contain database_workload.json")

        if not os.path.exists(f"{work_dir}/database_tuning_record.json"):
            raise FileNotFoundError(
                "Error: the found workdir does not contain database_tuning_record.json")

        if env.get('CM_TUNE_TVM_MODEL', '') != '':
            print("The \"tune-model\" variation is selected, but at the same time the path to the existing \"work_dir\" is also specified. The compiled model will be based on the found existing \"work_dir\".")
            env["CM_TUNE_TVM_MODEL"] = "no"
            
    

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_ORIGINAL_FILE_WITH_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']
    env['CM_ML_MODEL_FILE'] = 'model-tvm.so'
    env['CM_ML_MODEL_PATH'] = os.path.join(os.getcwd())
    env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(
        os.getcwd(), env['CM_ML_MODEL_FILE'])
    env['CM_ML_MODEL_FRAMEWORK'] = "tvm-" + env['CM_ML_MODEL_FRAMEWORK']
    if 'CM_ML_MODEL_INPUT_SHAPES' in env.keys():
        env['CM_ML_MODEL_INPUT_SHAPES'] = env['CM_ML_MODEL_INPUT_SHAPES'].replace(
            "BATCH_SIZE", env['CM_ML_MODEL_MAX_BATCH_SIZE'])
    if 'CM_TVM_FRONTEND_FRAMEWORK' in env and env['CM_TVM_FRONTEND_FRAMEWORK'] == 'pytorch':
        env['CM_PREPROCESS_PYTORCH'] = 'yes'
    return {'return':0}
