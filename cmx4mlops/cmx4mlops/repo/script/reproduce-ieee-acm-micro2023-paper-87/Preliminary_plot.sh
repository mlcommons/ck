#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsPreliminaryExperiments/

echo ""
echo "Please go to $(pwd) and check ClockhandsPreliminaryExperiments*.xlsx ."
echo "The procedure of generating charts are described on them."
