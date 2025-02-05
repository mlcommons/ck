#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

cd /shared/
bash ./in-docker-bash-scripts/copy-parsec-binaries.sh

test $? -eq 0 || exit 1
