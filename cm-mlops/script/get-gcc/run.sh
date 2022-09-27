#!/bin/bash

echo "${CM_GCC_BIN_WITH_PATH} --version"

${CM_GCC_BIN_WITH_PATH} --version > tmp-ver.out
test $? -eq 0 || exit 1

cat tmp-ver.out
