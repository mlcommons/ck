#!/bin/bash
cd ${CM_ROCM_BIN_WITH_PATH##*/}../
cat .info/version  > tmp-ver.out
test $? -eq 0 || exit 1
