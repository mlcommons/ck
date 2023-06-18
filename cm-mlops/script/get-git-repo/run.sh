#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

folder=${CM_GIT_CHECKOUT_FOLDER}
if [ ! -d ${folder} ]; then
  echo "******************************************************"
  echo "Cloning ${CM_GIT_REPO_NAME} from ${CM_GIT_URL}"
  echo "${CM_GIT_CLONE_CMD}";

  ${CM_GIT_CLONE_CMD}
  if [ "${?}" != "0" ]; then exit 1; fi


  if [ ! -z ${CM_GIT_SHA} ]; then

    echo ""
    cd ${folder}
    cmd="git checkout -b ${CM_GIT_SHA}"
    echo "$cmd"
    eval "$cmd"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi
else
  cd ${folder}
fi

if [ ${CM_GIT_PATCH} == "yes" ]; then
  patch_filename=${CM_GIT_PATCH_FILENAME}
  if [ ! -n ${CM_GIT_PATCH_FILENAMES} ]; then
    patchfile=${CM_GIT_PATCH_FILENAME:-"git.patch"}
    CM_GIT_PATCH_FILENAMES=$patchfile
  fi
  IFS=', ' read -r -a patch_files <<< ${CM_GIT_PATCH_FILENAMES}
  for patch_filename in "${patch_files[@]}"
  do
    echo "Applying patch ${SCRIPT_DIR}/patch/$patch_filename"
    git apply ${SCRIPT_DIR}/patch/"$patch_filename"
    if [ "${?}" != "0" ]; then exit 1; fi
  done
fi
cd "$CUR_DIR"
