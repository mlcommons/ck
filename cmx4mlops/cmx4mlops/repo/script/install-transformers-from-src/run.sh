#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

CUR_DIR=$PWD
echo $PWD
rm -rf transformers
cmd="cp -r ${CM_TRANSFORMERS_SRC_REPO_PATH} transformers"
echo "$cmd"
eval "$cmd"
cd transformers
rm -rf build

wget -nc --no-check-certificate https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/bert-99/pytorch-cpu/patches/transformers.patch
if [ "${?}" != "0" ]; then exit 1; fi
git apply transformers.patch
if [ "${?}" != "0" ]; then exit 1; fi

echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
