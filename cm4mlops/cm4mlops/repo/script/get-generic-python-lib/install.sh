#!/bin/bash

echo ""

if [[ ${CM_GENERIC_PYTHON_PACKAGE_VARIANT} == "nvidia-apex-depreciated" ]]; then
  cd ${CM_GIT_REPO_CHECKOUT_PATH}
  cmd="${CM_PYTHON_BIN_WITH_PATH} -m pip install -v --disable-pip-version-check --global-option=\"--cpp_ext\" --global-option=\"--cuda_ext\" ./"
  echo $cmd
  if [[ -n ${CM_PIP_ERROR_SKIP} ]]; then
    eval $cmd
  else
    eval $cmd
    test $? -eq 0 || exit $?
  fi
  exit 0
fi

if [[ ${CM_GENERIC_PYTHON_PACKAGE_NAME}  == "tensorflow_old" ]]; then
    if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
        if [[ -n ${CM_PIP_ERROR_SKIP} ]]; then
            . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-macos.sh
	else
            . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-macos.sh
            test $? -eq 0 || exit $?
        fi
        exit 0
    fi
    if [[ ${CM_HOST_PLATFORM_FLAVOR} == "aarch64" ]]; then
        if [[ -n ${CM_PIP_ERROR_SKIP} ]]; then
            . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-aarch64.sh
	else
            . ${CM_TMP_CURRENT_SCRIPT_PATH}/tensorflow/run-aarch64.sh
            test $? -eq 0 || exit $?
        fi
        exit 0
    fi
fi

if [[ -n ${CM_GENERIC_PYTHON_PIP_URL} ]]; then
    cmd="${CM_PYTHON_BIN_WITH_PATH} -m pip install \"${CM_GENERIC_PYTHON_PIP_URL}\" ${CM_GENERIC_PYTHON_PIP_EXTRA}"
    echo $cmd
    if [[ -n ${CM_PIP_ERROR_SKIP} ]]; then
        eval $cmd
    else
        eval $cmd
        test $? -eq 0 || exit $?
    fi
    exit 0
fi

cmd="${CM_PYTHON_BIN_WITH_PATH} -m pip install \"${CM_GENERIC_PYTHON_PACKAGE_NAME}${CM_TMP_PIP_VERSION_STRING}\" ${CM_GENERIC_PYTHON_PIP_EXTRA}"
echo $cmd

if [[ -n ${CM_PIP_ERROR_SKIP} ]]; then
    eval $cmd
else
    eval $cmd
    test $? -eq 0 || exit $?
fi
exit 0
