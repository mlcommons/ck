#!/bin/bash

CUR=${PWD}

WGET_URL="https://developer.download.nvidia.com/compute/cuda/"${CM_VERSION}"/local_installers/${CM_CUDA_LINUX_FILENAME}"

INSTALL_DIR=${CUR}/install

${CM_SUDO} bash ${CM_CUDA_RUN_FILE_PATH} --toolkitpath=${INSTALL_DIR} --defaultroot=${INSTALL_DIR}

