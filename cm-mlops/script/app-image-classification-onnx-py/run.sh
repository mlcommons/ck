#!/bin/bash

if [[ ${CM_RUN_DOCKER_CONTAINER} == "yes" ]]; then
  exit 0
fi

#echo ${CM_PYTHON_BIN}
#echo ${CM_DATASET_PATH}
#echo ${CM_DATASET_AUX_PATH}
#echo ${CM_ML_MODEL_FILE_WITH_PATH}
CM_PYTHON_BIN=${CM_PYTHON_BIN_WITH_PATH:-python3}
CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

# connect CM intelligent components with CK env
export CK_ENV_ONNX_MODEL_ONNX_FILEPATH=${CM_ML_MODEL_FILE_WITH_PATH}
export CK_ENV_ONNX_MODEL_INPUT_LAYER_NAME="input_tensor:0"
export CK_ENV_ONNX_MODEL_OUTPUT_LAYER_NAME="softmax_tensor:0"
export CK_ENV_DATASET_IMAGENET_VAL=${CM_DATASET_PATH}
export CK_CAFFE_IMAGENET_SYNSET_WORDS_TXT=${CM_DATASET_AUX_PATH}/synset_words.txt
export ML_MODEL_DATA_LAYOUT="NCHW"
export CK_BATCH_SIZE=${CM_BATCH_SIZE}
export CK_BATCH_COUNT=${CM_BATCH_COUNT}

if [[ "${CM_INPUT}" != "" ]]; then export CM_IMAGE=${CM_INPUT}; fi

PIP_EXTRA=`${CM_PYTHON_BIN} -c "import importlib.metadata; print(' --break-system-packages ' if int(importlib.metadata.version('pip').split('.')[0]) >= 23 else '')"`

echo ""
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt ${PIP_EXTRA}
test $? -eq 0 || exit 1

echo ""
${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/src/onnx_classify.py
test $? -eq 0 || exit 1

# Just a demo to pass environment variables from native scripts back to CM workflows
echo "CM_APP_IMAGE_CLASSIFICATION_ONNX_PY=sucess" > tmp-run-env.out
