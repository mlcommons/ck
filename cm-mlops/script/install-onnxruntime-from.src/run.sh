#!/bin/bash

cd ${CM_RUN_DIR}
echo ${CM_RUN_CMD}

eval ${CM_RUN_CMD}
test $? -eq 0 || exit $?

exit 1
