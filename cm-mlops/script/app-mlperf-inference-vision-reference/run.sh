#!/bin/bash

IFS="??" read -r -a cmd_array <<< "$CM_MLC_RUN_CMDS"
for cmd in "${cmd_array[@]}"
do
  echo "${cmd}"
  eval ${cmd}
  test $? -eq 0 || exit 1
done

echo "Starting Compliance Runs...";
IFS="??" read -r -a cmd_array <<< "$CM_MLC_COMPLIANCE_RUN_CMDS"
for cmd in "${cmd_array[@]}"
do
  echo "${cmd}"
  eval ${cmd}
  test $? -eq 0 || exit 1
done
