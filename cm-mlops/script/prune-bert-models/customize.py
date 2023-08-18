from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    ckpt_path = env.get('CM_BERT_PRUNE_CKPT_PATH','')
    if ckpt_path == '':
        p = env['CM_ML_MODEL_FILE_WITH_PATH']
        x = os.listdir(p)
        for y in x:
            if y.startswith('models--'):
                z = os.path.join(p,y)
                if os.path.isdir(z):
                    z1 = os.path.join(z, 'snapshots')
                    if os.path.isdir(z1):
                        z2 = os.listdir(z1)
                        if len(z2)>0:
                            ckpt_path=os.path.join(z1, z2[0])

    env['CM_BERT_PRUNE_CKPT_PATH'] = ckpt_path

    out_dir=env.get('CM_BERT_PRUNE_OUTPUT_DIR','')
    if out_dir == '':
        out_dir = os.path.join(os.getcwd(), 'pruned-model-output')
    env['CM_BERT_PRUNE_OUTPUT_DIR'] = out_dir

    print ('')
    print ('Local CM cache path to the updated BERT pruner src from NeurIPS 2022: ' + env['CM_GIT_REPO_BERT_PRUNER_NEURIPS_2022_CHECKOUT_PATH'])

    print ('')
    for k in ["CM_ML_MODEL_FILE_WITH_PATH", "CM_BERT_PRUNE_CKPT_PATH", "CM_BERT_PRUNE_OUTPUT_DIR"]:
        print ('ENV["{}"]: {}'.format(k, env[k]))

    print ('')

    return {'return': 0}

def postprocess(i):

    env = i['env']

    print("Entered postprocess")

    return {'return': 0}
