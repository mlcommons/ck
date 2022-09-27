#!/bin/bash

${CM_NVCC_BIN} -V > tmp-ver.out
test $? -eq 0 || exit 1
