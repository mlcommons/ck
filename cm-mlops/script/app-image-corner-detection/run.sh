#!/bin/bash

CUR=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
mkdir -p $CUR"/output"

test $? -eq 0 || exit 1
