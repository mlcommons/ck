#!/bin/bash
#${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_INFERENCE_VISION_PATH}/tools/retinanet_pytorch_to_onnx.py
#${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_INFERENCE_VISION_PATH}/tools/retinanet_pytorch_to_onnx.py --weights ${CM_ML_MODEL_FILE_WITH_PATH}
${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_TRAINING_SOURCE}/single_stage_detector/ssd/pth_to_onnx.py --num-classes 264 --image-size 800 800 --input ${CM_ML_MODEL_FILE_WITH_PATH} --output retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx
${CM_TMP_CURRENT_SCRIPT_PATH}/polygraphy_script.sh retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx folded.onnx backend.onnx nms.onnx
#CM_ML_MODEL_DYN_BATCHSIZE_PATH=`pwd`/retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx
#CM_ML_MODEL_PATCHED_PATH=`pwd`/test_fpn_efficientnms_concatall.onnx
#CM_ML_MODEL_ANCHOR_PATH=${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}/code/retinanet/tensorrt/onnx_generator/retinanet_anchor_xywh_1x1.npy

