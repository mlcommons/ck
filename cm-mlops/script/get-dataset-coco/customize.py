from cmind import utils
import os
import shutil

def preprocess(i):

    # CM script internal variables
    variation_tags = i.get('variation_tags',[])
    automation = i['automation']
    env = i['env']
    meta = i['meta']
    quiet = (env.get('CM_QUIET', False) == 'yes')

    # Check if path is there to detect existing data set
    detected = False
    path = env.get('CM_TMP_PATH','')
    if path!='':
        if not os.path.isdir(path):
            return {'return':1, 'error':'path to dataset "{}" doesn\'t exist'.format(path)}

        # Check which dataset
        p = os.path.join(path, 'annotations')
        if os.path.isdir(p):
            for d in [('val2017','val','2017'), 
                      ('train2017','train','2017')]:
                p = os.path.join(path, d[0])

                if os.path.isdir(p):
                    tp = d[1]
                    ver = d[2]
                    detected = True
                    break

        if not detected:
            return {'return':1, 'error':'COCO dataset is not detected in "{}"'.format(path)}

        print ('')
        print ('Detected COCO dataset {} {}'.format(tp,ver))
        
        env['CM_DATASET_COCO_DETECTED'] = 'yes'
        env['CM_DATASET_COCO_PATH'] = path
    else:
        ver = env['CM_DATASET_COCO_VERSION']
        tp = env['CM_DATASET_COCO_TYPE']

    # Prepare URL
    size=env.get('CM_DATASET_COCO_SIZE','')
    if size=='small' and tp=='val' and ver=='2017':
        # We prepared a small version with 50 images for val 2017

        filename_data = 'val2017_small.zip'
        filename_annotation = 'annotations_val2017_small.zip'

        url_data_full = 'https://www.dropbox.com/scl/fi/whokyb7b7hyjqqotruyqb/{}?rlkey=hhgt4xtir91ej0nro6h69l22s&dl=0'.format(filename_data)
        url_ann_full = 'https://www.dropbox.com/scl/fi/bu41y62v9zqhee8w7q6z3/{}?rlkey=seqtgozldkc0ztu76kbd47p5w&dl=0'.format(filename_annotation)

    else:
        url_data = env['CM_DATASET_COCO_URL_DATA']
        url_ann = env['CM_DATASET_COCO_URL_ANNOTATIONS']
        
        filename_data = tp + ver + '.zip'
        filename_annotation = 'annotations_trainval' + ver + '.zip'

        url_data_full = url_data + '/' + filename_data
        url_ann_full = url_ann + '/' + filename_annotation

    # Add extra tags with type and version to "download-and-extract" deps to be able to reuse them
    # Add "from" and "to" to "download-and-extract" deps
    download_extra_cache_tags='dataset,coco,data,'+tp+','+ver

    dae_input_data = {
      'extra_cache_tags':download_extra_cache_tags
    }
    dae_input_annotation = {
      'extra_cache_tags':download_extra_cache_tags
    }

    path_from = env.get('CM_FROM', '')
    if path_from!='':
        path_from_data = os.path.join(path_from, filename_data)
        if not os.path.isfile(path_from_data):
            return {'return':1, 'error':'File {} not found'.format(path_from_data)}
        dae_input_data['local_path'] = path_from_data

        path_from_annotation = os.path.join(path_from, filename_annotation)
        if not os.path.isfile(path_from_annotation):
            return {'return':1, 'error':'File {} not found'.format(path_from_annotation)}
        dae_input_annotation['local_path'] = path_from_annotation

    path_to = env.get('CM_TO', '')
    if path_to!='':
        dae_input_data['extract_path'] = path_to
        dae_input_annotation['extract_path'] = path_to
    
    path_store = env.get('CM_STORE', '')
    if path_store!='':
        dae_input_data['download_path'] = path_store
        dae_input_data['tags'] = '_keep'
        dae_input_annotation['download_path'] = path_store
        dae_input_annotation['tags'] = '_keep'

    
    r = automation.update_deps({'deps':meta['prehook_deps'],
                                'update_deps':{
                                  '746e5dad5e784ad6': dae_input_data,
                                  'edb6cd092ff64171': dae_input_annotation
                                }
                               })
    if r['return']>0: return r

    # Prepare environment variables
    env['CM_DATASET_COCO_VERSION'] = ver
    env['CM_DATASET_COCO_TYPE'] = tp
    env['CM_DATASET_COCO_TYPE_AND_VERSION'] = tp+ver
    env['CM_DATASET_COCO_URL_DATA_FULL'] = url_data_full
    env['CM_DATASET_COCO_URL_ANNOTATIONS_FULL'] = url_ann_full

    # Check MD5SUM
    md5sum_data = ''
    md5sum_ann = ''

    if ver == '2017':
        if tp == 'val':
            if size == 'small':
               md5sum_data = '16fab985a33afa66beeb987f68c2023c'
               md5sum_ann = '78c0cfd9fc32c825d4ae693fd0d91407'
            else:
               md5sum_data = '442b8da7639aecaf257c1dceb8ba8c80'
               md5sum_ann = 'f4bbac642086de4f52a3fdda2de5fa2c'

    if md5sum_data != '':
        env['CM_DATASET_COCO_MD5SUM_DATA'] = md5sum_data
    if md5sum_ann != '':
        env['CM_DATASET_COCO_MD5SUM_ANN'] = md5sum_ann

    if not detected:
        print ('')
        print ('URL for data: {}'.format(url_data_full))
        print ('URL for annotations: {}'.format(url_ann_full))

    # Add version and type to tags
    extra_cache_tags = []
    for tag in [ver, tp]:
        if tag not in variation_tags: 
            extra_cache_tags.append(tag)

    return {'return':0, 'add_extra_cache_tags':extra_cache_tags}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    tp_ver = env['CM_DATASET_COCO_TYPE_AND_VERSION']

    path_to = env.get('CM_TO','')
    
    # Check if detected or downloaded
    if env.get('CM_DATASET_COCO_DETECTED', '').lower() == 'yes' or path_to!='':
        path_all = env['CM_DATASET_COCO_PATH'] if path_to=='' else path_to

        env['CM_DATASET_COCO_DATA_PATH'] = os.path.join(path_all, tp_ver)
        env['CM_DATASET_COCO_ANNOTATIONS_PATH'] = os.path.join(path_all, 'annotations')
    else:
        path_all = os.getcwd()
    
        # Moving 2 directories to 1 place
        
        path_data = env['CM_DATASET_COCO_DATA_PATH']
        path_ann = env['CM_DATASET_COCO_ANNOTATIONS_PATH']

        print ('')
        print (path_all)
        print ('')

        path_data_full = os.path.join(path_data, tp_ver)
        path_ann_full = os.path.join(path_ann, 'annotations')

        if os_info['platform'] == 'windows':
            # Moving to this directory since can't make symbolic links
            command1 = '  move /y ' + path_data_full + ' ' + tp_ver
            command2 = '  move /y ' + path_ann_full + ' annotations' 

            env['CM_DATASET_COCO_DATA_PATH'] = os.path.join(path_all, tp_ver)
            env['CM_DATASET_COCO_ANNOTATIONS_PATH'] = os.path.join(path_all, 'annotations')
        else:
            # Make soft links from data and annotations into 1 directory 
            # (standard way for COCO)

            command1 = '  ln -s ' + path_data_full + ' ' + tp_ver
            command2 = '  ln -s ' + path_ann_full + ' annotations' 

        for command in [command1, command2]:
            print (command)
            os.system(command)


    env['CM_DATASET_COCO_PATH'] = path_all
    env['CM_DATASET_PATH'] = path_all
    env['CM_DATASET_PATH_ROOT'] = path_all

    return {'return': 0}
