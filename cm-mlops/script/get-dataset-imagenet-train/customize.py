from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_DATASET_IMAGENET_TRAIN_LOCAL_PATH'):
        path = env['CM_DATASET_IMAGENET_TRAIN_LOCAL_PATH']
        if path.endswith(".tar"):
            env['CM_DAE_FILEPATH'] = path
            env['CM_DATASET_IMAGENET_TRAIN_REQUIRE_EXTRACT'] = "yes"

    elif env.get('CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH'):
        path = env['CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH']
        env['CM_DAE_FILEPATH'] = path
        env['CM_DATASET_IMAGENET_TRAIN_REQUIRE_TORRENT'] = "yes"

        r = automation.update_deps({'deps':meta['prehook_deps'],
                                'update_deps':{
                                    'download-torrent':{
                                       'tags':"_torrent."+path
                                    }
                                }
            })
        if r['return'] > 0 return r
    else:
        print(i)
        return {'return':1, 'error': 'Imagenet dataset cannot be automatically downloaded from any public URL. Please provide a torrent path which you can get from https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5'}

    return {'return':0}

def postprocess(i):

    env = i['env']

    if env.get('CM_DATASET_IMAGENET_TRAIN_REQUIRE_EXTRACT', '') == "yes":
        env['CM_DATASET_IMAGENET_TRAIN_PATH'] = env['CM_DAE_FILE_DOWNLOADED_PATH']

    return {'return':0}
