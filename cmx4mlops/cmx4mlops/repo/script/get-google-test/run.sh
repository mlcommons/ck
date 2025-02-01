#!/bin/bash
function cmake() {
${CM_CMAKE_BIN_WITH_PATH} $@
}

export CC=${CM_C_COMPILER_WITH_PATH}
export CXX=${CM_CXX_COMPILER_WITH_PATH}

CUR=$PWD
mkdir -p install
INSTALL_DIR=$CUR/install
cd ${CM_GIT_REPO_CHECKOUT_PATH}

mkdir build
cd build
export MAKEFLAGS=-j${CM_MAKE_CORES}
cmake -DCMAKE_INSTALL_PREFIX=${INSTALL_DIR} ..
test $? -eq 0 || exit $?

CMD="make install"
echo ${CMD}
eval $CMD
test $? -eq 0 || exit $?
