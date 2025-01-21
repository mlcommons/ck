#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} --version > tmp-ver.out 2>&1
test $? -eq 0 || exit 1

#PYTHON_BIN_PATH="${python_bin%/*}"
#
#if [[ ! -f ${PYTHON_BIN_PATH}/python ]]; then
#  echo "Creating softlink of python to python3"
#  cmd="sudo ln -s ${python_bin} ${PYTHON_BIN_PATH}/python"
#  echo $cmd
#  eval $cmd
#fi
