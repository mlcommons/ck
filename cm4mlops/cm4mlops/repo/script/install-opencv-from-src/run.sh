#!/bin/bash

CUR_DIR=$PWD
rm -rf opencv
cp -r ${CM_OPENCV_SRC_REPO_PATH} opencv
cd opencv
test "${?}" -eq "0" || exit $?
rm -rf build

mkdir build
cd build
cmake ..
test "${?}" -eq "0" || exit $?
make  -j${CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET}
test "${?}" -eq "0" || exit $?
