#!/bin/bash

if [[ ${CM_GENERIC_PYTHON_PACKAGE_NAME}  == "tensorflow" ]]; then
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

if [[ -n ${CM_GENERIC_PYTHON_PIP_URL} ]]; then
    cmd="${CM_PYTHON_BIN_WITH_PATH} -m pip install ${CM_GENERIC_PYTHON_PIP_URL} ${CM_GENERIC_PYTHON_PIP_EXTRA}"
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit 1
    exit 0
fi

if [[ -n ${CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL} ]]; then
    CM_GENERIC_PYTHON_PIP_EXTRA="${CM_GENERIC_PYTHON_PIP_EXTRA} --extra-index-url ${CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL}"
fi

${CM_PYTHON_BIN_WITH_PATH} -m pip install ${CM_GENERIC_PYTHON_PACKAGE_NAME}${CM_TMP_PIP_VERSION_STRING} ${CM_GENERIC_PYTHON_PIP_EXTRA}
test $? -eq 0 || exit 1
