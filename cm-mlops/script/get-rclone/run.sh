#!/bin/bash
if ! command -v rclone &> /dev/null
then
  exit 1
fi
rclone --version > tmp-ver.out
test $? -eq 0 || exit 1
