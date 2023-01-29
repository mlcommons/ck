#!/bin/bash

if [[ -n ${CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS} ]]; then
    cmd="${CM_PYTHON_BIN_WITH_PATH} -m pip uninstall ${CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS} -y"
    echo "$cmd"
    eval "$cmd"
    test $? -eq 0 || exit $?
fi
