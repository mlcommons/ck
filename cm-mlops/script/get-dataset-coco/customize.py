from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    ver = env['CM_DATASET_COCO_VERSION']
    split = env['CM_DATASET_COCO_SPLIT']

    url_zips = env['CM_DATASET_COCO_URL_ZIPS']
    url_ann = env['CM_DATASET_COCO_URL_ANNOTATIONS']

    filename = split + ver + '.zip'

    url_zips_full = url_zips + '/' + filename
    url_ann_full = url_ann + '/annotations_trainval' + ver + '.zip'

    env['CM_DATASET_COCO_URL_ZIPS_FULL'] = url_zips_full
    env['CM_DATASET_COCO_URL_ANNOTATIONS_FULL'] = url_ann_full

    return {'return': 0}

def postprocess(i):

    return {'return': 0}
