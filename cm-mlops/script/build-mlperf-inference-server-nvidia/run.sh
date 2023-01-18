#!/bin/bash
CUR=$PWD
scratch_path=${MLPERF_SCRATCH_PATH}
mkdir ${scratch_path}/data
mkdir ${scratch_path}/preprocessed_data
mkdir ${scratch_path}/models

${CM_PYTHON_BIN_WITH_PATH} -m scripts.custom_systems.add_custom_system

export CXXFLAGS=" -Wno-error=switch"
