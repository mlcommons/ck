#!/bin/bash

echo ${PATH}

if ! command -v rclone &> /dev/null
then
  echo "rclone was not detected"
  exit 1
fi
rclone --version > tmp-ver.out
test $? -eq 0 || exit 1
