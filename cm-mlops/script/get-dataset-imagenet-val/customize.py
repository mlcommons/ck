from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':0}

    full = env.get('CM_IMAGENET_FULL', '').strip() == 'yes'

    path = env.get('CM_INPUT', env.get('IMAGENET_PATH', '')).strip()

    if path == '':
        if full:

            if env.get('CM_DATASET_IMAGENET_VAL_TORRENT_PATH'):
                path = env['CM_DATASET_IMAGENET_VAL_TORRENT_PATH']
                env['CM_DATASET_IMAGENET_VAL_REQUIRE_TORRENT'] = "yes"

                r = automation.update_deps({'deps':meta['prehook_deps'],
                    'update_deps':{
                        'download-torrent':{
                        'tags':"_torrent."+path
                        }
                    }
                })

                if r['return'] > 0: return r
                env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'
                env['CM_DAE_ONLY_EXTRACT'] = 'yes'

                return {'return':0}

            else:
                return {'return':1, 'error':'Please rerun the last CM command with --env.IMAGENET_PATH={path the folder containing full ImageNet images} or envoke cm run script "get val dataset imagenet" --input={path to the folder containing ImageNet images}'}

        else:
            env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'


    elif not os.path.isdir(path):
        if path.endswith(".tar"):
            env['CM_DAE_FILEPATH'] = path
            env['CM_DATASET_IMAGENET_VAL_REQUIRE_DAE'] = 'yes'
            env['CM_DAE_ONLY_EXTRACT'] = 'yes'
            return {'return':0}
        else:
            return {'return':1, 'error':'Path {} doesn\'t exist'.format(path)}
    else:
        env['CM_DAE_FILE_EXTRACTED_PATH'] = path

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':0}

    env = i['env']
    path = env['CM_DAE_FILE_EXTRACTED_PATH']

    path_image = os.path.join(path, 'ILSVRC2012_val_00000001.JPEG')

    if not os.path.isfile(path_image):
        return {'return':1, 'error':'ImageNet file {} not found'.format(path_image)}

    env['CM_DATASET_PATH'] = path
    env['CM_DATASET_IMAGENET_PATH'] = path
    env['CM_DATASET_IMAGENET_VAL_PATH'] = path

    return {'return':0}

