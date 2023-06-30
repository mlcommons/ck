#!/bin/bash
if [[ ${CM_CUDA_FULL_TOOLKIT_INSTALL} == "no" ]]; then
  exit 0
fi
nvcc_bin=${CM_NVCC_BIN_WITH_PATH:-nvcc}

${nvcc_bin} -V > tmp-ver.out
test $? -eq 0 || exit 1
