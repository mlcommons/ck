#!/bin/bash
CUR=$PWD
scratch_path=${MLPERF_SCRATCH_PATH}
mkdir -p ${scratch_path}/data
mkdir -p ${scratch_path}/preprocessed_data
mkdir -p ${scratch_path}/models

${CM_PYTHON_BIN_WITH_PATH} -m scripts.custom_systems.add_custom_system
test $? -eq 0 || $?
export CXXFLAGS=" -Wno-error=switch"
make build
test $? -eq 0 || $?
