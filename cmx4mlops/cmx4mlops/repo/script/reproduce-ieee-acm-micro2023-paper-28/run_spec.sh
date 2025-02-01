#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to XFM repo's SPEC2017 Directory: ${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment"
cd ${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment

./run.sh
test $? -eq 0 || exit 1

echo ""

mkdir -p ${CUR_DIR}/results/spec
test $? -eq 0 || exit 1

./parse.sh | tee ${CUR_DIR}/results/spec/results.txt
test $? -eq 0 || exit 1


