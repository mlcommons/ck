#!/bin/bash

CUR_DIR=$PWD
rm -rf pytorchvision
cp -r ${CM_PYTORCH_VISION_SRC_REPO_PATH} pytorchvision
cd pytorchvision
test "${?}" -eq "0" || exit $?
rm -rf build

${CM_PYTHON_BIN_WITH_PATH} setup.py bdist_wheel
test "${?}" -eq "0" || exit $?
cd dist
${CM_PYTHON_BIN_WITH_PATH} -m pip install torchvision*linux_x86_64.whl
test "${?}" -eq "0" || exit $?
