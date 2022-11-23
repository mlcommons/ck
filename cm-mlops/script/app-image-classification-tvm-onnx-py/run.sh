#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

#if [[ ${CM_HOST_PLATFORM_FLAVOR} == "arm64" ]]; then
#    ${CM_PYTHON_BIN} -m pip install -i https://test.pypi.org/simple/ onnxruntime==1.9.0.dev174552
#fi

export USE_TVM=yes


wget -nc https://raw.githubusercontent.com/mlcommons/ck-mlops/main/program/ml-task-image-classification-tvm-onnx-cpu/synset.txt
test $? -eq 0 || exit 1

${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1

if [[ "${CM_INPUT}" != "" ]]; then 
  export CM_IMAGE=${CM_INPUT}
else
  export CM_IMAGE=${CM_DATASET_PATH}/ILSVRC2012_val_00000001.JPEG
fi


${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/src/classify.py --image ${CM_IMAGE}
test $? -eq 0 || exit 1
