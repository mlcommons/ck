from cmind import utils
import os
import shutil

def preprocess(i):

    variation_tags = i.get('variation_tags',[])

    env = i['env']

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

    url_data = env['CM_DATASET_COCO_URL_DATA']
    url_ann = env['CM_DATASET_COCO_URL_ANNOTATIONS']

    
    filename = tp + ver + '.zip'

    url_data_full = url_data + '/' + filename
    url_ann_full = url_ann + '/annotations_trainval' + ver + '.zip'

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

    # Check if detected or downloaded
    if env.get('CM_DATASET_COCO_DETECTED', '').lower() == 'yes':
        path_all = env['CM_DATASET_COCO_PATH']

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
