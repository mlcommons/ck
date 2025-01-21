#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo ""

cd /shared/python-runners/
${CM_PYTHON_BIN_WITH_PATH} convert-gem5-results-to-csv.py

test $? -eq 0 || exit 1

cd /shared/paper-figures/

${CM_PYTHON_BIN_WITH_PATH} figure-1.py
${CM_PYTHON_BIN_WITH_PATH} figure-2.py
${CM_PYTHON_BIN_WITH_PATH} figure-4.py
${CM_PYTHON_BIN_WITH_PATH} figure-5.py
${CM_PYTHON_BIN_WITH_PATH} figure-6_7.py
${CM_PYTHON_BIN_WITH_PATH} figure-8_9.py
${CM_PYTHON_BIN_WITH_PATH} figure-10_11.py
${CM_PYTHON_BIN_WITH_PATH} figure-12.py
${CM_PYTHON_BIN_WITH_PATH} figure-13.py

test $? -eq 0 || exit 1
