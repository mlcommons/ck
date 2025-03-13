#!/bin/bash

CUR=${PWD}
rm -rf install
mkdir -p install

export DATASET_CNNDM_PATH=${CUR}/install

wget -nc https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/gptj-99/pytorch-cpu/download-dataset.py
test $? -eq 0 || exit 1

cmd="${CM_PYTHON_BIN_WITH_PATH} download-dataset.py --split validation --output-dir ${DATASET_CNNDM_PATH}"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit 1
