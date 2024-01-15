#!/bin/bash

curl -fsSL -v -o ~/miniconda.sh -O  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
test $? -eq 0 || exit $?
chmod +x ~/miniconda.sh

if [ ! -z ${CM_CONDA_PREFIX_NAME} ]; then
  CM_CONDA_INSTALL_PATH=$PWD/miniconda3
  rm -rf ${CM_CONDA_INSTALL_PATH}
fi


if [ ! -z ${CM_CONDA_INSTALL_PATH} ]; then
  ~/miniconda.sh -b -p ${CM_CONDA_INSTALL_PATH}
else
  ~/miniconda.sh -b
fi
test $? -eq 0 || exit $?
