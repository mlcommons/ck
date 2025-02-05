#!/bin/bash
CUR=$PWD
mkdir -p install
INSTALL_DIR=$CUR/install
cd ${CM_GIT_REPO_CHECKOUT_PATH}
rm -rf build
mkdir build
cd build
export MAKEFLAGS=-j${CM_MAKE_CORES}
cmake -Dprotobuf_BUILD_TESTS=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_PREFIX=${INSTALL_DIR} ../cmake
test $? -eq 0 || exit $?
CMD="make install"
echo ${CMD}
eval $CMD
test $? -eq 0 || exit $?
