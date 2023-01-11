#!/bin/bash
nvcc_bin=${CM_NVCC_BIN_WITH_PATH}

${nvcc_bin} -V > tmp-ver.out
test $? -eq 0 || exit 1
