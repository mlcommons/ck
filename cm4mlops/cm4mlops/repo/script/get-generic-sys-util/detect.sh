#!/bin/bash

if [[ -n "${CM_SYS_UTIL_VERSION_CMD_OVERRIDE}" ]]; then
  cmd="${CM_SYS_UTIL_VERSION_CMD_OVERRIDE}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit $?
else
  if [[ -n "${CM_SYS_UTIL_VERSION_CMD}" ]]; then
    if [[ "${CM_SYS_UTIL_VERSION_CMD_USE_ERROR_STREAM}" == "yes" ]]; then
      # Redirect both stdout and stderr to tmp-ver.out
      cmd="${CM_SYS_UTIL_VERSION_CMD} > tmp-ver.out 2>&1"
    else
      cmd="${CM_SYS_UTIL_VERSION_CMD} > tmp-ver.out"
    fi
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit $?
  fi
fi

