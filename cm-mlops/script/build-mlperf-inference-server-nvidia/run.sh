#!/bin/bash
CUR=$PWD
scratch_path=${CUR}
export MLPERF_SCRATCH_PATH=${scratch_path}
mkdir -p ${scratch_path}/data
mkdir -p ${scratch_path}/preprocessed_data
mkdir -p ${scratch_path}/models
cd ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}

#make clean
make build
test $? -eq 0 || exit $?
