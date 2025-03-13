#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to SPAM repo: ${CM_GIT_REPO_SPA_ARTIFACT_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_SPA_ARTIFACT_CHECKOUT_PATH}

echo ""

bash ./artifact-bash-scripts/set-up-docker.sh
test $? -eq 0 || exit 1
