#!/bin/bash
#${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_INFERENCE_VISION_PATH}/tools/retinanet_pytorch_to_onnx.py
#${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_INFERENCE_VISION_PATH}/tools/retinanet_pytorch_to_onnx.py --weights ${CM_ML_MODEL_FILE_WITH_PATH}
${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_TRAINING_SOURCE}/single_stage_detector/ssd/pth_to_onnx.py --num-classes 264 --image-size 800 800 --input ${CM_ML_MODEL_FILE_WITH_PATH} --output retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx
exit 1
