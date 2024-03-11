#!/bin/bash

CUR_DIR=$PWD
rm -rf pytorchvision
cp -r ${CM_PYTORCH_VISION_SRC_REPO_PATH} pytorchvision
cd pytorchvision
test "${?}" -eq "0" || exit $?
rm -rf build

python setup.py bdist_wheel
test "${?}" -eq "0" || exit $?
cd dist
python3 -m pip install torchvision*linux_x86_64.whl
test "${?}" -eq "0" || exit $?
