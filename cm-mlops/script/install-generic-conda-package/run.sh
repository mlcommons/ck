#!/bin/bash


cmd="${CM_CONDA_PKG_INSTALL_CMD}"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
