#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to GRAPE repo: ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}

echo ""

source scripts/Installation/activate

./scripts/Experiment_Workflow/1-test_metadata_compression.sh


test $? -eq 0 || exit 1
