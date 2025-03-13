#!/bin/bash
cmd=${CM_RUN_CMD}
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit $?

cmd=${CM_POST_RUN_CMD}
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit $?

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.py
test $? -eq 0 || exit $?
