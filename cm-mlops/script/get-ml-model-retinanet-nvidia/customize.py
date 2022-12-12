from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    if '+PYTHONPATH' not in env:
        env['+PYTHONPATH'] = []
    env['+PYTHONPATH'].append(os.path.join(env['CM_MLPERF_TRAINING_SOURCE'], "single_stage_detector", "ssd"))
    env['CM_ML_MODEL_DYN_BATCHSIZE_PATH'] = os.path.join(os.getcwd(), "retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx")
    if "CM_NVIDIA_EFFICIENT_NMS" in env:
        env['CM_NVIDIA_MODEL_PATCHED_PATH'] = os.path.join(os.getcwd(), "fpn_efficientnms_concatall.onnx")
        env['CM_ML_MODEL_ANCHOR_PATH'] = os.path.join(env['CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH'], "code", "retinanet", "tensorrt", "onnx_generator", "retinanet_anchor_xywh_1x1.npy")
    return {'return':0}

def postprocess(i):
    env = i['env']
    env['CM_NVIDIA_RETINANET_EFFICIENT_NMS_CONCAT_MODEL_WITH_PATH'] = os.path.join(os.getcwd(), "test_fpn_efficientnms_concatall.onnx")
    if "CM_NVIDIA_EFFICIENT_NMS" in env:
        env['CM_NVIDIA_RETINANET_EFFICIENT_NMS_CONCAT_MODEL_WITH_PATH'] = env['CM_NVIDIA_MODEL_PATCHED_PATH']
    return {'return':0}
