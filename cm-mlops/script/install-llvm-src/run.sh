#!/bin/bash

CUR_DIR=$PWD


if [ ! -d "llvm" ]; then
   echo "******************************************************"
   echo "Cloning LLVM from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

   git clone -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} llvm
   if [ "${?}" != "0" ]; then exit 1; fi
fi


INSTALL_DIR="${CUR_DIR}/install"

# If install exist, then configure was done 
if [ ! -d "${INSTALL_DIR}" ]; then
    echo "******************************************************"

    mkdir -p build
    cd build

    cmake \
        -DLLVM_ENABLE_PROJECTS=clang \
        -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
        -DCMAKE_BUILD_TYPE=Release \
        -DLLVM_ENABLE_RTTI=ON \
        -DLLVM_INSTALL_UTILS=ON \
        ../llvm/llvm
    if [ "${?}" != "0" ]; then exit 1; fi

    mkdir -p ${INSTALL_DIR}
fi

cd build

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

echo "Using ${CM_MAKE_CORES} cores ..."

cmake --build . --target install -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "LLVM was built and installed to ${INSTALL_DIR} ..."
