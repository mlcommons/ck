#!/bin/bash

cd ${ZENDNN_SRC_PATH}

make clean
test $? -eq 0 || exit $?

source scripts/zendnn_build.sh gcc
test $? -eq 0 || exit $?
