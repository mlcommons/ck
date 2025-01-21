#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to GRAPE repo: ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_GRAPE_MICRO56_CHECKOUT_PATH}

echo ""

. scripts/Installation/0-install_build_essentials.sh
test $? -eq 0 || exit 1
