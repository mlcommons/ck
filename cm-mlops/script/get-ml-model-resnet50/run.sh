#!/bin/bash
if [[ ${CM_TMP_WGET} == "yes" ]]; then
    wget -nc ${CM_PACKAGE_URL}
fi
if [[ ${CM_TMP_EXTRACT} == "yes" ]]; then
    cmd="gunzip ${CM_TMP_EXTRACT_FILE_NAME}" 
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit 1
fi
