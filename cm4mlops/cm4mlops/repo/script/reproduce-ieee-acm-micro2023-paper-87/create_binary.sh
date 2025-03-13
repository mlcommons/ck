#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsEvaluation/

sed s@~@..@ -i A-riscv/stuff/make.inc
cd A-riscv/coremark/
make
cd ../../

cd B-straight/toolchain/Test/coremark/
make
cd ../../../../

cd C-clockhands/coremark/
make
cd ../../
