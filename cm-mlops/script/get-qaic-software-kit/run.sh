#!/bin/bash

function cmake() {
${CM_CMAKE_BIN_WITH_PATH}
}

export -f cmake

cd ${CM_QAIC_SOFTWARE_KIT_PATH}
./bootstrap.sh
test $? -eq 0 || exit $?
cd build
../scripts/build.sh -b Release
test $? -eq 0 || exit $?
