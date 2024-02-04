#!/bin/bash

CUR_DIR=$PWD
rm -rf pytorch
cp -r ${CM_PYTORCH_SRC_REPO_PATH} pytorch
cd pytorch
git submodule sync
git submodule update --init --recursive
rm -rf build

${CM_PYTHON_BIN_WITH_PATH} -m pip install -r requirements.txt
if [ "${?}" != "0" ]; then exit $?; fi
${CM_PYTHON_BIN_WITH_PATH} setup.py bdist_wheel
test $? -eq 0 || exit $?
cd dist
${CM_PYTHON_BIN_WITH_PATH} -m pip install torch-2.*linux_x86_64.whl
test $? -eq 0 || exit $?
