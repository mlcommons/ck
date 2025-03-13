#!/bin/bash

CUR=${PWD}
INSTALL_DIR=${CUR}/install

echo "******************************************"
echo "${CUR}"
echo "${CM_CUDNN_TAR_FILE_PATH}"
echo "${CM_CUDNN_TAR_DIR}"
echo "${CM_CUDNN_UNTAR_PATH}"
echo "${CUDA_HOME}"
echo "${CM_CUDA_PATH_INCLUDE}"
echo "${CM_CUDA_PATH_LIB}"
echo "******************************************"

echo "Untaring file ..."
echo ""
tar -xf ${CM_CUDNN_TAR_FILE_PATH}
test $? -eq 0 || exit $?

echo "Copying include files ..."
echo ""
${CM_SUDO} cp -P ${CM_CUDNN_TAR_DIR}/include/cudnn*.h ${CM_CUDA_PATH_INCLUDE}
${CM_SUDO} chmod a+r ${CM_CUDA_PATH_INCLUDE}/cudnn*.h

echo "Copying lib files ..."
echo ""
${CM_SUDO} cp -P ${CM_CUDNN_TAR_DIR}/lib/libcudnn* ${CM_CUDA_PATH_LIB}
${CM_SUDO} chmod a+r ${CM_CUDA_PATH_LIB}/libcudnn*

echo "Adding file that cuDNN is installed ..."
echo ""
if [ "${CM_SUDO}" == "sudo" ]; then
  ${CM_SUDO} sh -c "echo '${CM_VERSION}' > ${CUDA_HOME}/cm_installed_cudnn.txt"
else
  echo "${CM_VERSION}" > ${CUDA_HOME}/cm_installed_cudnn.txt
fi
