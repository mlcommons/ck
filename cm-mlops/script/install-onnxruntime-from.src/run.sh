#!/bin/bash

echo "cd ${CM_RUN_DIR}"
cd ${CM_RUN_DIR}
test $? -eq 0 || exit $?
echo ${CM_RUN_CMD}

eval ${CM_RUN_CMD}
test $? -eq 0 || exit $?

exit 1
