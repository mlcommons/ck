#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning Mlperf Inference results from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."
folder_name="inference_results_${CM_MLPERF_INFERENCE_RESULTS_VERSION_NAME}"
if [ ! -d ${folder_name} ]; then
  if [ -z ${CM_GIT_SHA} ]; then
    git clone ${CM_GIT_RECURSE_SUBMODULES} -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} ${CM_GIT_DEPTH} ${folder_name}
    cd ${folder_name}
  else
    git clone ${CM_GIT_RECURSE_SUBMODULES} ${CM_GIT_URL} ${CM_GIT_DEPTH} ${folder_name}
    cd ${folder_name}
    git checkout -b "${CM_GIT_CHECKOUT}"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi
fi

if [ ${CM_GIT_PATCH} == "yes" ]; then
  patch_filename=${CM_GIT_PATCH_FILENAME:-git.patch}
  echo "Applying patch ${SCRIPT_DIR}/patch/$patch_filename"
  git apply ${SCRIPT_DIR}/patch/"$patch_filename"
  if [ "${?}" != "0" ]; then exit 1; fi
fi
cd "$CUR_DIR"
