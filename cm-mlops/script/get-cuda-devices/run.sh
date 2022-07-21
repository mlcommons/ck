#!/bin/bash

# Compile

rm a.out

echo ""
echo "Checking compiler version ..."
echo ""

${CM_NVCC_BIN} -V

echo ""
echo "Compiling program ..."
echo ""

cd ${CM_TMP_CURRENT_SCRIPT_PATH}

${CM_NVCC_BIN} print_cuda_devices.cu
test $? -eq 0 || exit 1

# Return to the original path obtained in CM

echo ""
echo "Running program ..."
echo ""

cd ${CM_TMP_CURRENT_PATH}

${CM_TMP_CURRENT_SCRIPT_PATH}/a.out
test $? -eq 0 || exit 1
