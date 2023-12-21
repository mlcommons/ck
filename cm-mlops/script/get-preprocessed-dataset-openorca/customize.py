from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']
    inference_src = env['CM_MLPERF_INFERENCE_SOURCE']

    run_dir = os.path.join(inference_src, 'language', 'llama2-70b')
    model_dir = env['CM_ML_MODEL_PATH']
    run_cmd = env['CM_PYTHON_BIN_WITH_PATH'] + ' processorca.py --dataset_pq_path=' + env['CM_DATASET_OPENORCA_PARQUET'] + ' --model_dir=' + model_dir +' --seqlen_limit=2048 --export_dir=' + os.path.join(os.getcwd(), "processed-openorca") + ' --num_total_samples=' + env['CM_DATASET_SIZE']

    env['CM_RUN_DIR'] = run_dir
    env['CM_RUN_CMD'] = run_cmd



    return {'return': 0}

def postprocess(i):
    env = i['env']
    env['CM_DATASET_PREPROCESSED_PATH'] = os.path.join(os.path.join(os.getcwd(), "processed-openorca", 'open_orca_gpt4_tokenized_llama.sampled_'+env['CM_DATASET_SIZE']+'.pkl'))

    return {'return': 0}
