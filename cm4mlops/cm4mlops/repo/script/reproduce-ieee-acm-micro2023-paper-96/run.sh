#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to Victima repo: ${CM_GIT_REPO_CMU_SAFARI_VICTIMA_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_CMU_SAFARI_VICTIMA_CHECKOUT_PATH}

echo ""

sh artifact.sh --${CM_VICTIMA_JOB_MANAGER} ${CM_VICTIMA_CONTAINER}
test $? -eq 0 || exit 1
