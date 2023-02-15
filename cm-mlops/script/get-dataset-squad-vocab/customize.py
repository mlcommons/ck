from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    env = i['env']

    env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH'] = os.path.join(os.getcwd(), 'vocab.txt')
    env['CM_DATASET_SQUAD_VOCAB_PATH'] = os.path.join(os.getcwd(), 'vocab.txt')

    return {'return':0}
