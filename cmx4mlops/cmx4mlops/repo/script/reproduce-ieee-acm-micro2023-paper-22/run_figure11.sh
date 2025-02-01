#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to GRAPE repo: ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}

echo ""

source scripts/Installation/activate

./scripts/Experiment_Workflow/2-test_runtime_performance.sh --model=gpt2
./scripts/Experiment_Workflow/2-test_runtime_performance.sh --model=gptj
./scripts/Experiment_Workflow/2-test_runtime_performance.sh --model=wav2vec2

test $? -eq 0 || exit 1
