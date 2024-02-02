#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

CUR_DIR=$PWD
rm -rf pytorch
cp -r ${CM_PYTORCH_SRC_REPO_PATH} pytorch
cd pytorch
rm -rf build

git submodule sync
git submodule update --init --recursive
if [ "${?}" != "0" ]; then exit $?; fi

python3 -m pip install -r requirements.txt
python setup.py bdist_wheel
if [ "${?}" != "0" ]; then exit $?; fi
cd dist
python3 -m pip install torch-2.*linux_x86_64.whl
if [ "${?}" != "0" ]; then exit $?; fi
