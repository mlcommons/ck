from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    skip_preprocessing = False
    if env.get('CM_DATASET_PREPROCESSED_PATH', '') != '':
        '''
        Path with preprocessed dataset given as input
        '''
        skip_preprocessing = True
        print("Using preprocessed criteo dataset from '" + env['CM_DATASET_PREPROCESSED_PATH'] +"'")

    if not skip_preprocessing and env.get('CM_DATASET_PREPROCESSED_OUTPUT_PATH','') != '':
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    if not skip_preprocessing and env.get('CM_DATASET_CRITEO_MULTIHOT', '') == 'yes':
        i['run_script_input']['script_name'] = "run-multihot"
        #${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/preprocess.py
        output_dir = env['CM_DATASET_PREPROCESSED_PATH']
        dataset_path = env['CM_DATASET_PATH']
        tmp_dir = os.path.join(output_dir, "tmp")
        run_dir = os.path.join(env['CM_MLPERF_TRAINING_SOURCE'], "recommendation_v2", "torchrec_dlrm", "scripts")
        env['CM_RUN_CMD'] = f'cd {run_dir} && bash ./process_Criteo_1TB_Click_Logs_dataset.sh {dataset_path} {tmp_dir} {output_dir} '

        print("Using MLCommons Training source from '" + env['CM_MLPERF_TRAINING_SOURCE'] +"'")

    return {'return': 0}
