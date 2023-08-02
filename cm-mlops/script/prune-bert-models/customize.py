from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    env['BERT_PRUNE_REPO_PATH'] = env['CM_GIT_CHECKOUT_PATH']
    print("Pruning repo path:"+env['BERT_PRUNE_REPO_PATH'])
    env['CM_UNPRUNED_MODEL_PATH']=env['CM_ML_MODEL_FILE_WITH_PATH']+"models--bert-large-uncased/snapshots/80792f8e8216b29f3c846b653a0ff0a37c210431"
    out_dir="/home/ubuntu/prune_model/out"
    cmd = "python3 "+env['BERT_PRUNE_REPO_PATH']+"/main.py --model_name " + env['CM_PRUNE_MODEL_NAME'] + " --task_name " + env['CM_PRUNE_TASK'] +  " --ckpt_dir "+env['CM_UNPRUNED_MODEL_PATH']+" --constraint 0.5 --output_dir "+out_dir
    os.system(cmd)
    return {'return': 0}

def postprocess(i):

    env = i['env']

    print("Entered postprocess")

    return {'return': 0}
