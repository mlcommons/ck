#!/bin/bash

${CM_GCC_BIN_WITH_PATH} --version > tmp-ver.out
test $? -eq 0 || exit 1
