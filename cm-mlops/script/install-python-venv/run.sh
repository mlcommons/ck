#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} -m pip install virtualenv
test $? -eq 0 || exit 1

${CM_PYTHON_BIN_WITH_PATH} -m venv venv
test $? -eq 0 || exit 1
