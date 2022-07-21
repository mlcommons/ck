#!/bin/bash

echo "CM_SOURCE_FOLDER_PATH=${CM_TMP_CURRENT_SCRIPT_PATH}" >> tmp-run-env.out
echo 'CM_C_SOURCE_FILES="susan.c"' >> tmp-run-env.out
echo 'CM_BIN_NAME=image-corner' >> tmp-run-env.out
CUR=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
mkdir -p $CUR"/output"
OUT=${CUR}/output

CM_INPUT=${CM_INPUT:-${CUR}/data.pgm}
CM_OUTPUT=${CM_OUTPUT:-output_image_with_corners.pgm}
echo "CM_RUN_DIR=${OUT}" >> tmp-run-env.out
echo "CM_RUN_SUFFIX=${CM_INPUT} ${CM_OUTPUT} -c" >> tmp-run-env.out

test $? -eq 0 || exit 1
