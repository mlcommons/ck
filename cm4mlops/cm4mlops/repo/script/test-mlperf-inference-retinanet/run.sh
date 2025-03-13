#!/bin/bash

echo ""

cd ${CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH}

ln -s ${CM_DATASET_PATH_ROOT}/annotations ${CM_DATASET_PATH_ROOT}/validation/data/annotations

${CM_PYTHON_BIN_WITH_PATH} python/main.py --profile retinanet-onnxruntime --scenario Offline --model ${CM_ML_MODEL_FILE_WITH_PATH} --dataset-path ${CM_DATASET_PATH_ROOT}/validation/data --accuracy
