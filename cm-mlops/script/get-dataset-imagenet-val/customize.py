from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    automation = i['automation']
    meta = i['meta']
    os_info = i['os_info']

    env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'no'

    full = env.get('CM_IMAGENET_FULL', '').strip() == 'yes'

    path = env.get('CM_INPUT', env.get('IMAGENET_PATH', env.get('CM_DATASET_IMAGENET_PATH', ''))).strip()

    if path == '':
        if full:

            if env.get('CM_DATASET_IMAGENET_VAL_TORRENT_PATH'):
                path = env['CM_DATASET_IMAGENET_VAL_TORRENT_PATH']
                env['CM_DAE_EXTRA_TAGS'] = "_torrent"
                env['CM_DAE_TORRENT_PATH'] = path
                env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'
                return {'return':0}

            else:
                env['CM_DAE_URL'] = 'https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar'
                env['CM_DAE_FILENAME'] = 'ILSVRC2012_img_val.tar'
                env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'

                return {'return':0}
                #return {'return':1, 'error':'Please rerun the last CM command with --env.IMAGENET_PATH={path the folder containing full ImageNet images} or envoke cm run script "get val dataset imagenet" --input={path to the folder containing ImageNet images}'}

        else:
            env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'


    elif not os.path.isdir(path):
        if path.endswith(".tar"):
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

    env = i['env']
    path = env['CM_EXTRACT_EXTRACTED_PATH']
    path1 = os.path.join(path, 'imagenet-2012-val')
    if os.path.isdir(path1):
        path = path1

    path_image = os.path.join(path, 'ILSVRC2012_val_00000001.JPEG')

    if not os.path.isfile(path_image):
        return {'return':1, 'error':'ImageNet file {} not found'.format(path_image)}

    files = os.listdir(path)
    if len(files) < int(env.get('CM_DATASET_SIZE', 0)):
        return {'return':1, 'error':'Only {} files found in {}. {} expected'.format(len(files), path, env.get('CM_DATASET_SIZE'))}

    env['CM_DATASET_PATH'] = path
    env['CM_DATASET_IMAGENET_PATH'] = path
    env['CM_DATASET_IMAGENET_VAL_PATH'] = path

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  path

    return {'return':0}

