from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']
    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    if env.get('CM_DATASET_CRITEO_MULTIHOT', '') == 'yes':
        i['run_script_input']['script_name'] = "run-multihot"
        if os.path.exists(os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "day_23_sparse_multi_hot.npz")):
            env['CM_RUN_CMD'] = ''
        else:
            output_dir = env['CM_DATASET_PREPROCESSED_PATH']
            tmp_dir = os.path.join(output_dir, "tmp")
            run_dir = os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "recommendation", "dlrm_v2", "pytorch", "tools")
            env['CM_RUN_CMD'] = f'cd {run_dir} && bash ./process_criteo_1TB_Click_Logs_dataset.sh {dataset_path} {tmp_dir} {output_dir} '

    print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    return {'return': 0}
