#!/bin/bash
CUR=$PWD

cd ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}

if [[ ${CM_MAKE_CLEAN} == "yes" ]]; then
  make clean
fi

if [[ ${CM_MLPERF_DEVICE} == "inferentia" ]]; then
 make prebuild
fi

SKIP_DRIVER_CHECK=1 make ${CM_MAKE_BUILD_COMMAND}

test $? -eq 0 || exit $?
