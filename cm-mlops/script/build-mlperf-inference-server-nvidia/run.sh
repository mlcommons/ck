#!/bin/bash
CUR=$PWD
scratch_path=${CUR}
export MLPERF_SCRATCH_PATH=${scratch_path}
mkdir -p ${scratch_path}/data
mkdir -p ${scratch_path}/preprocessed_data
mkdir -p ${scratch_path}/models
cd ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}

if [[ ${CM_MAKE_CLEAN} == "yes" ]]; then
  make clean
fi

if [[ ${CM_MLPERF_DEVICE} == "inferentia" ]]; then
 make prebuild
fi

make ${CM_MAKE_BUILD_COMMAND}

test $? -eq 0 || exit $?
