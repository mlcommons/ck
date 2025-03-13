#!/bin/bash

INSTALL_DIR=${CM_CUDA_INSTALL_PREFIX}/install

cmd="${CM_SUDO} bash ${CM_CUDA_RUN_FILE_PATH} --toolkitpath=${INSTALL_DIR} --defaultroot=${INSTALL_DIR} --toolkit ${CUDA_ADDITIONAL_INSTALL_OPTIONS} --silent --override ${CM_CUDA_EXTRA_INSTALL_ARGS}"
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit $?
