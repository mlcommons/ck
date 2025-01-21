#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to XFM repo: ${CM_GIT_REPO_XFM_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_XFM_CHECKOUT_PATH}

echo ""

cd memory_channel_interleave_ratios

./run.sh
test $? -eq 0 || exit 1

mkdir -p ${CUR_DIR}/results/memory_channel_interleave_ratios
test $? -eq 0 || exit 1

cp results.csv ${CUR_DIR}/results/memory_channel_interleave_ratios
test $? -eq 0 || exit 1
