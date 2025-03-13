#!/bin/bash

CUR=${PWD}
INSTALL_DIR=${CUR}/install

echo "******************************************"
echo "${CUR}"
echo "${CM_CUSPARSELT_TAR_FILE_PATH}"
echo "${CM_CUSPARSELT_TAR_DIR}"
echo "${CM_CUSPARSELT_UNTAR_PATH}"
echo "${CUDA_HOME}"
echo "${CM_CUDA_PATH_INCLUDE}"
echo "${CM_CUDA_PATH_LIB}"
echo "******************************************"

echo "Untaring file ..."
echo ""
tar -xf ${CM_CUSPARSELT_TAR_FILE_PATH}
test $? -eq 0 || exit $?

echo "Copying include files ..."
echo ""
${CM_SUDO} cp -P ${CM_CUSPARSELT_TAR_DIR}/include/cusparseLt*.h ${CM_CUDA_PATH_INCLUDE}
${CM_SUDO} chmod a+r ${CM_CUDA_PATH_INCLUDE}/cusparseLt*.h

echo "Copying lib files ..."
echo ""
${CM_SUDO} cp -P ${CM_CUSPARSELT_TAR_DIR}/lib/libcusparseLt* ${CM_CUDA_PATH_LIB}
${CM_SUDO} chmod a+r ${CM_CUDA_PATH_LIB}/libcusparseLt*

echo "Adding file that CUSPARSELT is installed ..."
echo ""
if [ "${CM_SUDO}" == "sudo" ]; then
  ${CM_SUDO} sh -c "echo '${CM_VERSION}' > ${CUDA_HOME}/cm_installed_cusparselt.txt"
else
  echo "${CM_VERSION}" > ${CUDA_HOME}/cm_installed_cusparselt.txt
fi
