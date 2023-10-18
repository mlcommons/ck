from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    datadir = env.get('CM_DATA_DIR', os.getcwd())
    env['CM_DATA_DIR'] = datadir

    env['MXNET_VER'] = env.get('CM_MXNET_VER', '22.08').replace("-", ".")

    env['CM_IMAGENET_LABELS_DOWNLOAD_DIR'] = env['CM_DATASET_IMAGENET_TRAIN_PATH']
    
    if env.get("CM_TMP_VARIATION", "") == "nvidia":
        code_path = os.path.join(env['CM_NVIDIA_DEEPLEARNING_EXAMPLES_REPO_PATH'], 'MxNet', 'Classification', 'RN50v1.5')
        env['CM_RUN_DIR'] = code_path
        i['run_script_input']['script_name'] = "run-nvidia"

    elif env.get("CM_TMP_VARIATION", "") == "reference":
        code_path = os.path.join(env['CM_MLPERF_TRAINING_SOURCE'], 'image_classification', 'tensorflow2')
        env['CM_RUN_DIR'] = code_path
        i['run_script_input']['script_name'] = "run-reference"

    return {'return':0}

def postprocess(i):

    env = i['env']

    data_dir = env['CM_DATA_DIR']
    env['CM_MLPERF_TRAINING_RESNET_DATA_PATH'] = data_dir

    env['CM_MLPERF_TRAINING_IMAGENET_PATH'] = env['CM_DATASET_IMAGENET_TRAIN_PATH']

    if env.get("CM_TMP_VARIATION", "") == "nvidia":
        env['CM_GET_DEPENDENT_CACHED_PATH'] = data_dir
        env['CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH'] = data_dir

    elif env.get("CM_TMP_VARIATION", "") == "reference":
        env['CM_GET_DEPENDENT_CACHED_PATH'] = os.path.join(data_dir, "tfrecords")
        env['CM_MLPERF_TRAINING_RESNET_TFRECORDS_PATH'] = os.path.join(data_dir, "tfrecords")

    return {'return':0}
