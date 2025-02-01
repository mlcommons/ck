#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to GRAPE repo: ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}

echo ""

source scripts/Installation/activate

. ${CM_TMP_CURRENT_SCRIPT_PATH}/run_figure13.sh
. ${CM_TMP_CURRENT_SCRIPT_PATH}/run_figure11.sh
. ${CM_TMP_CURRENT_SCRIPT_PATH}/run_figure12.sh


test $? -eq 0 || exit 1
