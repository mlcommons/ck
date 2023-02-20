#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."

if [ ! -d ${CM_GIT_REPO_FOLDER_NAME} ]; then
  if [ -z ${CM_GIT_SHA} ]; then
    git clone ${CM_GIT_RECURSE_SUBMODULES} -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} ${CM_GIT_DEPTH} ${CM_GIT_REPO_FOLDER_NAME}
    cd ${CM_GIT_REPO_FOLDER_NAME}
  else
    git clone ${CM_GIT_RECURSE_SUBMODULES} ${CM_GIT_URL} ${CM_GIT_DEPTH} ${CM_GIT_REPO_FOLDER_NAME}
    cd ${CM_GIT_REPO_FOLDER_NAME}
    git checkout -b "${CM_GIT_CHECKOUT}"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi
else
  cd ${CM_GIT_REPO_FOLDER_NAME}
fi

if [ ${CM_GIT_PATCH} == "yes" ]; then
  patch_filename=${CM_GIT_PATCH_FILENAME:-git.patch}
  echo "Applying patch ${SCRIPT_DIR}/patch/$patch_filename"
  git apply ${SCRIPT_DIR}/patch/"$patch_filename"
  if [ "${?}" != "0" ]; then exit 1; fi
fi
cd "$CUR_DIR"
cd ${CM_GIT_REPO_FOLDER_NAME}
#./setup.py install --user
