from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    automation = i['automation']
    meta = i['meta']
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':0}

    env['CM_DATASET_IMAGENET_TRAIN_REQUIRE_DAE'] = 'no'

    path = env.get('CM_INPUT', env.get('IMAGENET_TRAIN_PATH', '')).strip()

    if path == '':
        if env.get('CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH'):
            path = env['CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH']
            env['CM_DAE_EXTRA_TAGS'] = "_torrent"
            env['CM_DAE_TORRENT_PATH'] = path
            env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'

            return {'return':0}

        else:
            return {'return':1, 'error':'Please rerun the last CM command with --env.IMAGENET_TRAIN_PATH={path the folder containing full ImageNet training images} or envoke cm run script "get train dataset imagenet" --input={path to the folder containing ImageNet training images}'}


    elif not os.path.isdir(path):
        if path.endswith(".tar"):
            #env['CM_DAE_FILEPATH'] = path
            env['CM_EXTRACT_FILEPATH'] = path
            env['CM_DAE_ONLY_EXTRACT'] = 'yes'
            return {'return':0}
        else:
            return {'return':1, 'error':'Path {} doesn\'t exist'.format(path)}
    else:
        env['CM_EXTRACT_EXTRACTED_PATH'] = path

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':0}

    env = i['env']

    path = env['CM_EXTRACT_EXTRACTED_PATH']

    path_tar = os.path.join(path, 'n01440764.tar')

    if not os.path.isfile(path_tar):
        return {'return':1, 'error':'ImageNet file {} not found'.format(path_tar)}

    env['CM_DATASET_PATH'] = path
    env['CM_DATASET_IMAGENET_PATH'] = path
    env['CM_DATASET_IMAGENET_TRAIN_PATH'] = path

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  path

    return {'return':0}
