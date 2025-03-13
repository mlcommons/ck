#!/bin/bash

CUR=$PWD
echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}
test $? -eq 0 || exit $?
