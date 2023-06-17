from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    datadir = env.get('CM_DATA_DIR', os.getcwd())
    env['CM_DATA_DIR'] = datadir

    env['CM_BERT_CONFIG_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")
    env['CM_BERT_VOCAB_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")
    env['CM_BERT_DATA_DOWNLOAD_DIR'] = os.path.join(datadir, "download")
    
    env['CM_BERT_CHECKPOINT_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")

    if env.get("CM_TMP_VARIATION", "") == "nvidia":
        code_path = os.path.join(env['CM_GIT_REPO_CHECKOUT_PATH'], 'NVIDIA', 'benchmarks', 'bert', 'implementations', 'pytorch-22.09')
        env['CM_RUN_DIR'] = code_path
    elif env.get("CM_TMP_VARIATION", "") == "reference":
        code_path = os.path.join(env['CM_MLPERF_TRAINING_SOURCE'], 'language_model', 'tensorflow', 'bert', 'cleanup_scripts')
        env['CM_RUN_DIR'] = code_path

    return {'return':0}

def postprocess(i):

    env = i['env']

    data_dir = env['CM_DATA_DIR']
    env['CM_MLPERF_TRAINING_BERT_DATA_PATH'] = data_dir

    if env.get("CM_TMP_VARIATION", "") == "nvidia":
        env['CM_GET_DEPENDENT_CACHED_PATH'] = os.path.join(data_dir, "hdf5", "eval", "eval_all.hdf5")
    elif env.get("CM_TMP_VARIATION", "") == "reference":
        env['CM_GET_DEPENDENT_CACHED_PATH'] = os.path.join(data_dir, "tfrecords", "eval_10k")
        env['CM_MLPERF_TRAINING_BERT_TFRECORDS_PATH'] = os.path.join(data_dir, "tfrecords")

    env['CM_MLPERF_TRAINING_BERT_VOCAB_PATH'] = env['CM_BERT_VOCAB_FILE_PATH']
    env['CM_MLPERF_TRAINING_BERT_CONFIG_PATH'] = env['CM_BERT_CONFIG_FILE_PATH']

    return {'return':0}
