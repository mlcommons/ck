#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsPreliminaryExperiments/

cd raytracing.github.io/build_micro2023_ae/
sed s@~@../../../../ClockhandsEvaluation/A-riscv@ -i common.mk
make
cd ../../
cp raytracing.github.io/build_micro2023_ae/InOneWeekend/a.out onikiri2/benchmark/RayTracing/riscv64/bin/InOneWeekend
cp raytracing.github.io/build_micro2023_ae/TheNextWeek/a.out onikiri2/benchmark/RayTracing/riscv64/bin/TheNextWeek
cp raytracing.github.io/build_micro2023_ae/TheRestOfYourLife/a.out onikiri2/benchmark/RayTracing/riscv64/bin/TheRestOfYourLife
