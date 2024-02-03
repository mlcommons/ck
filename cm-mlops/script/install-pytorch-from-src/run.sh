#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH
export LD_LIBRARY_PATH="" #Don't use conda libs

CUR_DIR=$PWD
rm -rf pytorch
cp -r ${CM_PYTORCH_SRC_REPO_PATH} pytorch
cd pytorch
rm -rf build

python -m pip install -r requirements.txt
if [ "${?}" != "0" ]; then exit $?; fi
python setup.py bdist_wheel
test $? -eq 0 || exit $?
cd dist
python -m pip install torch-2.*linux_x86_64.whl
test $? -eq 0 || exit $?
