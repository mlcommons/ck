#!/bin/bash

if [[ ${CM_PYTHON_PACKAGE_NAME}  == "tensorflow" ]]; then
    if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
        . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-macos.sh
        test $? -eq 0 || exit 1
        exit 0
    fi
    if [[ ${CM_HOST_PLATFORM_FLAVOR} == "aarch64" ]]; then
        . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-aarch64.sh
        test $? -eq 0 || exit 1
        exit 0
    fi
fi

if [[ -n ${CM_PIP_URL} ]]; then
    ${CM_PYTHON_BIN_WITH_PATH} -m pip install ${CM_PIP_URL}
    test $? -eq 0 || exit 1
    exit 0
fi

${CM_PYTHON_BIN_WITH_PATH} -m pip install ${CM_PYTHON_PACKAGE_NAME}${CM_TMP_PIP_VERSION_STRING}
test $? -eq 0 || exit 1
