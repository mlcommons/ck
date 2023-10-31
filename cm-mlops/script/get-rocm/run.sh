#!/bin/bash

dir="${CM_ROCM_BIN_WITH_PATH%/*}/../"
cat ${dir}/.info/version  > tmp-ver.out
test $? -eq 0 || exit 1
