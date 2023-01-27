from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    if 'CM_ML_MODEL_FILE_WITH_PATH' in env:
        if 'CM_VOCAB_FILE_URL' in env:
            vocab_url = env['CM_VOCAB_FILE_URL']
            from urllib.parse import urljoin

            env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH']=os.path.join(path, env['CM_ML_MODEL_VOCAB_TXT'])

            print ('Downloading vocab file from {}'.format(vocab_url))
            r = cm.access({'action':'download_file',
                   'automation':'utils,dc2743f8450541e3',
                   'url':vocab_url})
            if r['return']>0: return r

        return {'return': 0}

    url = env['CM_PACKAGE_URL']
    if not url:
        return {'return':1, 'error': 'No valid URL to download the model. Probably an unsupported model variation chosen'}

    print ('Downloading from {}'.format(url))

    r = cm.access({'action':'download_file',
                   'automation':'utils,dc2743f8450541e3',
                   'url':url})
    if r['return']>0: return r

    if env.get('CM_UNTAR') == "yes":
        filename = r['filename']
        r  = os.system("tar -xvf "+filename)
        if r > 0:
            return {'return': r, 'error': 'Untar failed'}

        filename = env['CM_ML_MODEL_FILE']
        env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, filename)

    else:
        env['CM_ML_MODEL_FILE']=r['filename']
        env['CM_ML_MODEL_FILE_WITH_PATH']=r['path']
    env['CM_ML_MODEL_PATH']=path

    if 'CM_VOCAB_FILE_URL' in env:
        vocab_url = env['CM_VOCAB_FILE_URL']
    else:
        from urllib.parse import urljoin
        vocab_url = urljoin(url, env['CM_ML_MODEL_VOCAB_TXT'])

    env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH']=os.path.join(path, env['CM_ML_MODEL_VOCAB_TXT'])

    print ('Downloading vocab file from {}'.format(vocab_url))
    r = cm.access({'action':'download_file',
                   'automation':'utils,dc2743f8450541e3',
                   'url':vocab_url})
    if r['return']>0: return r


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return': 0}
