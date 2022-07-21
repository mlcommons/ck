#!/bin/bash
CUR=${PWD}
WGET_URL="https://developer.download.nvidia.com/compute/cuda/"${CM_VERSION}"/local_installers/cuda_"$CM_VERSION"_515.43.04_linux.run"
INSTALL_DIR=${CUR}/install
wget ${WGET_URL}
sh cuda_${CM_VERSION}"_515.43.04_linux.run" --toolkitpath=${INSTALL_DIR} --defaultroot=${INSTALL_DIR}

