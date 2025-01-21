#!/bin/bash

#export PATH=${CM_CONDA_BIN_PATH}:$PATH
#export LIBRARY_PATH=${CM_CONDA_LIB_PATH}:$LIBRARY_PATH

CUR_DIR=$PWD
rm -rf pytorch
cp -r ${CM_PYTORCH_SRC_REPO_PATH} pytorch
cd pytorch
rm -rf build

git submodule sync
git submodule update --init --recursive
if [ "${?}" != "0" ]; then exit 1; fi
pip install -r requirements.txt

cmd="${CM_RUN_CMD}"
echo ${cmd}
eval ${cmd}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
