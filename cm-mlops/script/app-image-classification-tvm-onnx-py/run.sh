#!/bin/bash

#echo ${CM_PYTHON_BIN}
#echo ${CM_DATASET_PATH}
#echo ${CM_DATASET_AUX_PATH}
#echo ${CM_ML_MODEL_FILE_WITH_PATH}

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
if [[ ${CM_HOST_PLATFORM_FLAVOR} == "arm64" ]]; then
    ${CM_PYTHON_BIN} -m pip install -i https://test.pypi.org/simple/ onnxruntime==1.9.0.dev174552
else
    ${CM_PYTHON_BIN} -m pip install onnxruntime
fi

# connect CM intelligent components with CK env
export CK_ENV_ONNX_MODEL_ONNX_FILEPATH=${CM_ML_MODEL_FILE_WITH_PATH}
export CK_ENV_ONNX_MODEL_INPUT_LAYER_NAME="input_tensor:0"
export CK_ENV_ONNX_MODEL_OUTPUT_LAYER_NAME="softmax_tensor:0"
export CK_ENV_DATASET_IMAGENET_VAL=${CM_DATASET_PATH}
export CK_CAFFE_IMAGENET_SYNSET_WORDS_TXT=${CM_DATASET_AUX_PATH}/synset_words.txt
export ML_MODEL_DATA_LAYOUT="NCHW"
export CK_BATCH_SIZE=${CM_BATCH_SIZE}
export CK_BATCH_COUNT=${CM_BATCH_COUNT}
export USE_TVM=yes


wget -nc https://raw.githubusercontent.com/mlcommons/ck-mlops/main/program/ml-task-image-classification-tvm-onnx-cpu/synset.txt
test $? -eq 0 || exit 1
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1

if [[ "${CM_INPUT}" != "" ]]; then 
  export CM_IMAGE=${CM_INPUT}
else
  export CM_IMAGE=${CK_ENV_DATASET_IMAGENET_VAL}/ILSVRC2012_val_00000001.JPEG
fi


${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/src/classify.py --image ${CM_IMAGE}
test $? -eq 0 || exit 1
