#!/bin/bash

CUR_DIR=$PWD
echo $PWD
rm -rf neural-speed
cmd="cp -r ${CM_INTEL_NEURAL_SPEED_SRC_REPO_PATH} neural-speed"
echo "$cmd"
eval "$cmd"
${CM_PYTHON_BIN_WITH_PATH} -m pip install -r neural-speed/requirements.txt
test $? -eq 0 || exit $?
CMAKE_ARGS="-DNS_PROFILING=ON" ${CM_PYTHON_BIN_WITH_PATH} -m pip install -ve ./neural-speed
test $? -eq 0 || exit $?

echo "******************************************************"
