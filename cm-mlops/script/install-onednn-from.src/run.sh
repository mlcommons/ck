#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

CUR_DIR=$PWD
rm -rf onednn
cp -r ${CM_ONEDNN_SRC_REPO_PATH} onednn
cd onednn
rm -rf build
pwd
wget -nc --no-check-certificate https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/bert-99/pytorch-cpu/patches/onednnv2_6.patch
if [ "${?}" != "0" ]; then exit 1; fi
git apply onednnv2_6.patch
if [ "${?}" != "0" ]; then exit 1; fi
pip install -r requirements.txt

mkdir build
pushd build
cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang -DBUILD_TPPS_INTREE=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="$(dirname $(python3 -c 'import torch; print(torch.__file__)'));../cmake/Modules" -GNinja -DUSERCP=ON ..
ninja
popd

#cmd="${CM_RUN_CMD}"
echo ${cmd}
eval ${cmd}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
