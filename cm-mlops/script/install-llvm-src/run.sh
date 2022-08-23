#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"
echo "Cloning LLVM from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "llvm" ]; then
  git clone -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} llvm
  if [ "${?}" != "0" ]; then exit 1; fi
fi

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

cmake \
    -DLLVM_ENABLE_PROJECTS=clang \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_INSTALL_UTILS=ON \
    ../llvm/llvm
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

echo "******************************************************"
echo "LLVM was built and installed to ${INSTALL_DIR} ..."
