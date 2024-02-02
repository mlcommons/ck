#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

CUR_DIR=$PWD
rm -rf pytorch
cp -r ${CM_PYTORCH_SRC_REPO_PATH} pytorch
cd pytorch
rm -rf build

git submodule sync
git submodule update --init --recursive
if [ "${?}" != "0" ]; then exit 1; fi
pushd third_party/gloo
wget -nc --no-check-certificate https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/bert-99/pytorch-cpu/patches/gloo.patch
if [ "${?}" != "0" ]; then exit 1; fi
git apply gloo.patch
if [ "${?}" != "0" ]; then exit 1; fi
popd

pushd third_party/ideep/mkl-dnn
wget -nc --no-check-certificate https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/bert-99/pytorch-cpu/patches/clang_mkl_dnn.patch
if [ "${?}" != "0" ]; then exit 1; fi
git apply clang_mkl_dnn.patch
if [ "${?}" != "0" ]; then exit 1; fi
popd

wget -nc --no-check-certificate https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/bert-99/pytorch-cpu/patches/pytorch_official_1_12.patch
if [ "${?}" != "0" ]; then exit 1; fi
git apply pytorch_official_1_12.patch
if [ "${?}" != "0" ]; then exit 1; fi
pip install -r requirements.txt

cmd="${CM_RUN_CMD}"
echo ${cmd}
eval ${cmd}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
