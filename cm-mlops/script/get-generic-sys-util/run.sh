#!/bin/bash

cmd=${CM_SYS_UTIL_INSTALL_CMD}
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
