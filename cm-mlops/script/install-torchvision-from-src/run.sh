#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

CUR_DIR=$PWD
rm -rf pytorchvision
cp -r ${CM_PYTORCH_VISION_SRC_REPO_PATH} pytorchvision
cd pytorchvision
if [ "${?}" != "0" ]; then exit $?; fi
rm -rf build

python setup.py bdist_wheel
if [ "${?}" != "0" ]; then exit $?; fi
cd dist
python3 -m pip install torchvision*linux_x86_64.whl
if [ "${?}" != "0" ]; then exit $?; fi
