#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_RUN_PYTHON_CMD}
test $? -eq 0 || exit $?
