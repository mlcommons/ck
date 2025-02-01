#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsEvaluation/

cp A-riscv/coremark/rvbin/coremark.rvbin evaluation/0.coremark
cp B-straight/toolchain/Test/coremark/stbin/coremark.stbin evaluation/0.coremark
cp C-clockhands/coremark/chbin/coremark.chbin evaluation/0.coremark
cp onikiri2/project/gcc/onikiri2/a.out evaluation/onikiri2
