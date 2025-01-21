#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
${CM_CXX_COMPILER_WITH_PATH} -O3 ${CM_TMP_CURRENT_SCRIPT_PATH}/src/classification.cpp -o classification.exe -ltensorflow

test $? -eq 0 || exit 1
