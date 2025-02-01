#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"
echo "ENV PIP_REQUIREMENTS: ${PIP_REQUIREMENTS}"
echo "ENV CM_VAR1: ${CM_VAR1}"

if [ "${PIP_REQUIREMENTS}" == "True" ]; then
  if test -f "${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt"; then
    echo ""
    echo "Installing requirements.txt ..."
    echo ""

    ${CM_PYTHON_BIN_WITH_PATH} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
    test $? -eq 0 || exit 1
  fi
fi

echo ""
${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/main.py
test $? -eq 0 || exit 1
