#!/bin/bash

CUR_DIR=$PWD


INSTALL_DIR="${CUR_DIR}/install"
echo "INSTALL_DIR=${INSTALL_DIR}"

rm -rf "${INSTALL_DIR}"
mkdir -p build
#rm -rf build

# If install exist, then configure was done 
if [ ! -d "${INSTALL_DIR}" ]; then
    echo "******************************************************"

    cd build

    echo "${CM_LLVM_CMAKE_CMD}"
    eval "${CM_LLVM_CMAKE_CMD}"
    ninja
    ninja install
    if [ "${?}" != "0" ]; then exit 1; fi

    mkdir -p ${INSTALL_DIR}
fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "LLVM is built and installed to ${INSTALL_DIR} ..."
