#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning Mlcommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "inference" ]; then
  git clone --recurse-submodules -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} inference
  if [ "${?}" != "0" ]; then exit 1; fi
fi

if [ ${CM_GIT_PATCH} ]; then
  echo "Applying patch ${SCRIPT_DIR}/patch/git.patch"
  cd inference
  git apply ${SCRIPT_DIR}/patch/git.patch
  git commit -a -m "Change for overriding OUTPUT_DIR for reference implementation"
fi
