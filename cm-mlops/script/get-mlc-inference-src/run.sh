#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning Mlcommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."

if [ ! -d "inference" ]; then
  git clone ${CM_GIT_RECURSE_SUBMODULES} -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} ${CM_GIT_DEPTH} inference
  if [ "${?}" != "0" ]; then exit 1; fi
  if [ -z ${CM_GIT_RECURSE_SUBMODULES} ]; then #needed to build loadgen
    cd inference
    git submodule update --init third_party/pybind
    cd ..
  fi
fi

if [ ${CM_GIT_PATCH} == "yes" ]; then
  echo "Applying patch ${SCRIPT_DIR}/patch/git.patch"
  cd inference
  git apply ${SCRIPT_DIR}/patch/git.patch
  git commit -a -m "Change for overriding OUTPUT_DIR for reference implementation"
  if [ "${?}" != "0" ]; then exit 1; fi
fi
