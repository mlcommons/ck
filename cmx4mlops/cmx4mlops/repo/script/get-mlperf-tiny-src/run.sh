#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning MLCommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES} ..."

if [ ! -d "src" ]; then
  if [ -z ${CM_GIT_SHA} ]; then
    git clone ${CM_GIT_RECURSE_SUBMODULES} -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} ${CM_GIT_DEPTH} src
    cd src
  else
    git clone ${CM_GIT_RECURSE_SUBMODULES} ${CM_GIT_URL} ${CM_GIT_DEPTH} src
    cd src
    git checkout -b "${CM_GIT_CHECKOUT}"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi
else
    cd src
fi

IFS=',' read -r -a submodules <<< "${CM_GIT_SUBMODULES}"

for submodule in "${submodules[@]}"
do
    echo "Initializing submodule ${submodule}"
    git submodule update --init "${submodule}"
    if [ "${?}" != "0" ]; then exit 1; fi
done

if [ ${CM_GIT_PATCH} == "yes" ]; then
  patch_filename=${CM_GIT_PATCH_FILENAME:-git.patch}
  echo "Applying patch ${SCRIPT_DIR}/patch/$patch_filename"
  git apply ${SCRIPT_DIR}/patch/"$patch_filename"
  if [ "${?}" != "0" ]; then exit 1; fi
fi

cd "$CUR_DIR"
