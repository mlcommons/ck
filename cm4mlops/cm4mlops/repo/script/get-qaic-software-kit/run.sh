#!/bin/bash

function cmake() {
${CM_CMAKE_BIN_WITH_PATH} $@
}

export CC=${CM_C_COMPILER_WITH_PATH}
export CXX=${CM_CXX_COMPILER_WITH_PATH}

export -f cmake
cd ${CM_QAIC_SOFTWARE_KIT_PATH}
rm -rf build
./bootstrap.sh
test $? -eq 0 || exit $?
cd build
../scripts/build.sh -b Release
test $? -eq 0 || exit $?
