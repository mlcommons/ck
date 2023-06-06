from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')
    if env.get("CM_TMP_VARIATION", "") == "nvidia":
        datadir = env.get('CM_DATA_DIR', os.getcwd())
        env['CM_BERT_CONFIG_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")
        env['CM_BERT_VOCAB_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")
        env['CM_BERT_DATA_DOWNLOAD_DIR'] = os.path.join(datadir, "download")
    
        env['CM_BERT_CHECKPOINT_DOWNLOAD_DIR'] = os.path.join(datadir, "phase1")
        code_path = os.path.join(env['CM_GIT_REPO_CHECKOUT_PATH'], 'NVIDIA', 'benchmarks', 'bert', 'implementations', 'pytorch-22.09')
        env['CM_RUN_DIR'] = code_path

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':1}
