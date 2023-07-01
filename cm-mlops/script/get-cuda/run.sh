#!/bin/bash
if [[ ${CM_CUDA_FULL_TOOLKIT_INSTALL} == "no" ]]; then
  exit 0
fi
nvcc_bin=${CM_NVCC_BIN_WITH_PATH:-nvcc}

${nvcc_bin} -V > tmp-ver.out
test $? -eq 0 || exit 1

if [[ ${nvcc_bin} == "nvcc" ]]; then
  nvcc_path=`which nvcc`
  echo "CM_NVCC_BIN_WITH_PATH=${nvcc_path}" >> tmp-run-env.out
  test $? -eq 0 || exit 1
fi
