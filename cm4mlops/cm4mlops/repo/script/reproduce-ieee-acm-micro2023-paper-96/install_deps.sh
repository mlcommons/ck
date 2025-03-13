#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "Changing to Victima repo: ${CM_GIT_REPO_CMU_SAFARI_VICTIMA_CHECKOUT_PATH}"
cd ${CM_GIT_REPO_CMU_SAFARI_VICTIMA_CHECKOUT_PATH}

if test -f "${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt"; then
  echo ""
  echo "Installing requirements.txt ..."
  echo ""

  ${CM_PYTHON_BIN_WITH_PATH} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
  test $? -eq 0 || exit 1
fi

echo ""

sh install_docker.sh
test $? -eq 0 || exit 1
