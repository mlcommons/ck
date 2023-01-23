#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"

if [ ! -d "cmsis" ]; then
  if [ -z ${CM_GIT_SHA} ]; then
    echo "Cloning CMSIS_5 from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."
    git clone ${CM_GIT_RECURSE_SUBMODULES} -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} ${CM_GIT_DEPTH} cmsis
    if [ "${?}" != "0" ]; then exit 1; fi
  else
    echo "Cloning CMSIS_5 from ${CM_GIT_URL} with default branch and checkout ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."
    git clone ${CM_GIT_RECURSE_SUBMODULES} ${CM_GIT_URL} ${CM_GIT_DEPTH} cmsis
    if [ "${?}" != "0" ]; then exit 1; fi
    cd cmsis
    git checkout "${CM_GIT_CHECKOUT}"
    if [ "${?}" != "0" ]; then exit 1; fi
  fi
fi
