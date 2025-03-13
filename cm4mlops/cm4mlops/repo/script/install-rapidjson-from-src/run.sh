#!/bin/bash

CUR_DIR=$PWD
rm -rf rapidjson
cp -r ${CM_RAPIDJSON_SRC_REPO_PATH} rapidjson
cd rapidjson
test "${?}" -eq "0" || exit $?
rm -rf build

mkdir build
cd build
cmake ..
test "${?}" -eq "0" || exit $?
make  -j${CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET}
test "${?}" -eq "0" || exit $?
