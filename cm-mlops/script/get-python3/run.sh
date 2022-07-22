#!/bin/bash

CM_PYTHON_BIN_WITH_PATH=${CM_PYTHON_BIN_WITH_PATH:-python3}
${CM_PYTHON_BIN_WITH_PATH} --version > tmp-ver.out
test $? -eq 0 || exit 1

PYTHON_BIN_PATH="${CM_PYTHON_BIN_WITH_PATH%/*}"

if [[ ! -f ${PYTHON_BIN_PATH}/python ]]; then
  echo "Creating softlink of python to python3"
  echo "sudo ln -s ${CM_PYTHON_BIN_WITH_PATH} ${PYTHON_BIN_PATH}/python"
  sudo ln -s ${CM_PYTHON_BIN_WITH_PATH} ${PYTHON_BIN_PATH}/python
fi
