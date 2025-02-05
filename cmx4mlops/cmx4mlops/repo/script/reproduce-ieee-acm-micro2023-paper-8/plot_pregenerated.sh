#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_GIT_REPO_FPSG_UIUC_TEAAL_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_FPSG_UIUC_TEAAL_CHECKOUT_PATH}

docker-compose run cl scripts/plot_pregenerated.sh

test $? -eq 0 || exit 1

