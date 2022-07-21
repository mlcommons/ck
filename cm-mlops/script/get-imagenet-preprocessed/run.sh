#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1

wget -nc https://raw.githubusercontent.com/mlcommons/ck-mlops/main/program/ml-task-image-classification-tvm-onnx-cpu/synset.txt
test $? -eq 0 || exit 1

mkdir preprocessed

${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/src/classify.py --image ${CM_DATASET_PATH}/ILSVRC2012_val_00000001.JPEG 
test $? -eq 0 || exit 1

cd preprocessed && ls *.raw > names.txt && cd ../
test $? -eq 0 || exit 1

echo "CM_DATASET_PREPROCESSED_PATH=$PWD/preprocessed" > tmp-run-env.out
