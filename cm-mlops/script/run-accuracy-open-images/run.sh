#!/bin/bash

IFS="??" read -r -a cmd_array <<< "$CM_RUN_CMDS"
for cmd in "${cmd_array[@]}"
do
  echo "${cmd}"
  eval ${cmd}
  test $? -eq 0 || exit 1
done
