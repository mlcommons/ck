#!/bin/bash
if [[ ${CM_TMP_EXTRACT} == "yes" ]]; then
    wget -nc ${CM_PACKAGE_URL}
    cmd="gunzip ${CM_TMP_EXTRACT_FILE_NAME}" 
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit 1
fi
