#!/bin/bash

cmd="wget -nc ${CM_WGET_URL} --no-check-certificate"
echo $cmd
eval $cmd
cmd="unzip ${CM_WGET_ZIP_FILE_NAME}"
echo $cmd
eval $cmd
test $? -eq 0 || exit 1
