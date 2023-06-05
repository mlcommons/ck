#!/bin/bash

wget -nc ${CM_WGET_URL} --no-check-certificate
test $? -eq 0 || exit 1

unzip ${CM_TMP_ZIP_FILE_NAME}
test $? -eq 0 || exit 1

