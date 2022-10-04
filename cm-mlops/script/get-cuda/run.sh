#!/bin/bash
nvcc_bin=${CM_CUDA_INSTALLED_PATH}/${FILE_NAME}
nvcc_bin=${CM_NVCC_BIN_WITH_PATH:-${nvcc_bin}}

${nvcc_bin} -V > tmp-ver.out
test $? -eq 0 || exit 1
