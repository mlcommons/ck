#!/bin/bash

CUR=${PWD}

WGET_URL="https://developer.download.nvidia.com/compute/cuda/"${CM_VERSION}"/local_installers/${CM_CUDA_LINUX_FILENAME}"

INSTALL_DIR=${CUR}/install

wget -nc ${WGET_URL}

${CM_SUDO} bash ${CM_CUDA_LINUX_FILENAME} --toolkitpath=${INSTALL_DIR} --defaultroot=${INSTALL_DIR}

