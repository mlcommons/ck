#!/bin/bash
if [ ${CM_TMP_RUN_COPY_SCRIPT} == "yes" ]; then
    cmd="${CM_SUDO} cp   ${CM_TMP_INC_PATH}/*.h   ${CM_CUDA_PATH_INCLUDE}/"
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit 1

    cmd="${CM_SUDO} cp -P ${CM_TMP_LIB_PATH}/libcudnn* ${CM_CUDA_PATH_LIB}/"
    echo $cmd
    eval $cmd
    test $? -eq 0 || exit 1
fi
