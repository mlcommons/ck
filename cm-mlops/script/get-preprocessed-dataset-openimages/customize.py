from cmind import utils
import os
import shutil
import glob

def preprocess(i):

    env = i['env']

    if 'CM_DATASET_PREPROCESSED_PATH' not in env:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()

    if env.get('CM_DATASET_REFERENCE_PREPROCESSOR',"0") == "1":
        print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

    if env.get('CM_ML_MODEL_NAME', '') == 'retinanet':
        if env.get('CM_DATASET_QUANTIZE', '') == '1':
            if env.get('CM_QAIC_MODEL_RETINANET_IMAGE_SCALE', '') != '':
                env['CM_DATASET_QUANT_SCALE'] = env['CM_QAIC_MODEL_RETINANET_IMAGE_SCALE']
            if env.get('CM_QAIC_MODEL_RETINANET_IMAGE_OFFSET', '') != '':
                env['CM_DATASET_QUANT_OFFSET'] = env['CM_QAIC_MODEL_RETINANET_IMAGE_OFFSET']

    return {'return': 0}

def postprocess(i):

    env = i['env']

    if env["CM_DATASET_TYPE"] == "validation":
        env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "annotations")
        env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-mlperf.json")

    # finalize path
    preprocessed_path = env['CM_DATASET_PREPROCESSED_PATH']
    preprocessed_images_list = []
    preprocessed_imagenames_list = []

    match_text = "/*."+env.get("CM_DATASET_PREPROCESSED_EXTENSION","*")
    for filename in sorted(glob.glob(preprocessed_path + match_text)):
        preprocessed_images_list.append(filename)
        preprocessed_imagenames_list.append(os.path.basename(filename))
    with open("preprocessed_files.txt", "w") as f:
        f.write("\n".join(preprocessed_images_list))
    with open("preprocessed_filenames.txt", "w") as f:
        f.write("\n".join(preprocessed_imagenames_list))

    env['CM_DATASET_PREPROCESSED_IMAGES_LIST'] = os.path.join(os.getcwd(), "preprocessed_files.txt")
    env['CM_DATASET_PREPROCESSED_IMAGENAMES_LIST'] = os.path.join(os.getcwd(), "preprocessed_filenames.txt")

    return {'return': 0}
