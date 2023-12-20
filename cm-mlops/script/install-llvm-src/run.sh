#!/bin/bash

CUR_DIR=$PWD


INSTALL_DIR="${CUR_DIR}/install"

# If install exist, then configure was done 
if [ ! -d "${INSTALL_DIR}" ]; then
    echo "******************************************************"

    mkdir -p build
    cd build

    ${CM_LLVM_CMAKE_CMD}

    if [ "${?}" != "0" ]; then exit 1; fi

    mkdir -p ${INSTALL_DIR}
fi


if [ "${CM_RENEW_CACHE_ENTRY}" != "yes" ]; then

    echo "******************************************************"
    CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
    CM_MAKE_CORES=${CM_MAKE_CORES:-2}

    echo "Using ${CM_MAKE_CORES} cores ..."

    cd build
    cmake --build . --target install -j${CM_MAKE_CORES}
    if [ "${?}" != "0" ]; then exit 1; fi
fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "LLVM is built and installed to ${INSTALL_DIR} ..."
