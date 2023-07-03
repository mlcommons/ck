#!/bin/bash

CUR=${PWD}

INSTALL_DIR=${CUR}/install

${CM_SUDO} bash ${CM_CUDA_RUN_FILE_PATH} --toolkitpath=${INSTALL_DIR} --defaultroot=${INSTALL_DIR} --toolkit --silent

