from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    cmds = []

    if env['CM_MODEL'] == "resnet50":
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'imagenet')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {env['CM_DATASET_IMAGENET_PATH']} {target_data_path}")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'ResNet50', 'resnet50_v1.onnx')
        model_name = "resnet50"

    elif "bert" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'squad')
        if not os.path.exists(target_data_path):
            cmds.append("make download_data BENCHMARKS='bert'")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'bert_large_v1_1.onnx')
        model_name = "bert"

    elif env['CM_MODEL'] == "retinanet":
        #print(env)
        dataset_path = env['CM_DATASET_PATH']
        #return {'return': 1, 'error': 'error'}

        annotations_path = env['CM_DATASET_ANNOTATIONS_DIR_PATH']
        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'annotations')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {annotations_path} {target_data_path}")

        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf', 'validation')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {dataset_path} {target_data_path}")

        calibration_dataset_path=env['CM_CALIBRATION_DATASET_PATH']
        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf','calibration', 'train')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {calibration_dataset_path} {target_data_path}")

        preprocessed_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'preprocessed_data')
        model_path = env['CM_NVIDIA_RETINANET_EFFICIENT_NMS_CONCAT_MODEL_WITH_PATH']
        target_model_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'retinanet-resnext50-32x4d', 'submission')
        if not os.path.exists(target_model_path_dir):
            cmds.append(f"mkdir -p {target_model_path_dir}")
        target_model_path = os.path.join(target_model_path_dir, 'retinanet_resnext50_32x4d_efficientNMS.800x800.onnx')
        if not os.path.exists(target_model_path):
            cmds.append(f"ln -sf {model_path} {target_model_path}")
        model_name = "retinanet"

    if not env.get('CM_SKIP_MODEL_DOWNLOAD', 'no') == "yes" and not os.path.exists(model_path):
        cmds.append(f"make download_model BENCHMARKS='{model_name}'")
    if not env.get('CM_SKIP_PREPROCESS_DATASET', 'no') == "yes":
        cmds.append(f"make preprocess_data BENCHMARKS='{model_name}'")
    scenario=env['CM_MLPERF_LOADGEN_SCENARIO'].lower()
    if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy":
        test_mode = "AccuracyOnly"
    elif env['CM_MLPERF_LOADGEN_MODE'] == "performance":
        test_mode = "PerformanceOnly"
    cmds.append(f"make run RUN_ARGS=' --benchmarks={model_name} --scenarios={scenario} --test_mode={test_mode}'")

    env['RUN_CMD'] = " && ".join(cmds)
#    print(env)

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}
