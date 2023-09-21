#!/bin/bash

if [[ ${CM_SUDO_USER} == "yes" ]]; then
  sudo dmidecode -t memory > meminfo.out
  ${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/get_memory_info.py
fi
test $? -eq 0 || return $?
