from cmind import utils
import os
from os.path import exists
import shutil
import glob

def preprocess(i):

    env = i['env']
    if 'CM_IMAGENET_PREPROCESSED_PATH' in env:
        files = glob.glob(env['CM_IMAGENET_PREPROCESSED_PATH']+"/**/"+env['CM_IMAGENET_PREPROCESSED_FILENAME'], recursive = True)
        if files:
            env['CM_DATASET_PREPROCESSED_PATH'] = env['CM_IMAGENET_PREPROCESSED_PATH']
        else:
            return {'return': 1, 'error': 'No preprocessed images found in '+env['CM_IMAGENET_PREPROCESSED_PATH']}
    else:
        print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

        if 'CM_DATASET_PREPROCESSED_PATH' not in env:
            env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()
        if not exists(os.path.join(env['CM_DATASET_PATH'], "val_map.txt")):
            shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), os.path.join(env['CM_DATASET_PATH'],
            "val_map.txt"))

    preprocessed_path = env['CM_DATASET_PREPROCESSED_PATH']
    
    if not exists(os.path.join(preprocessed_path, "val_map.txt")):
        shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), 
                    os.path.join(preprocessed_path, "val_map.txt"))


    return {'return': 0}

def postprocess(i):

    env = i['env']

    # finalize path
    preprocessed_path = env['CM_DATASET_PREPROCESSED_PATH']
    img_format = os.environ.get('CM_ML_MODEL_DATA_LAYOUT', 'NHWC')
    preprocessed_images_list = []
    for filename in glob.glob(preprocessed_path+"/*."+env.get("CM_NEW_EXTENSION","*")):
        preprocessed_images_list.append(filename)
    with open("preprocessed_files.txt", "w") as f:
        f.write("\n".join(preprocessed_images_list))

    env['CM_DATASET_PREPROCESSED_IMAGES_LIST'] = os.path.join(os.getcwd(), "preprocessed_files.txt")

    return {'return':0}
