#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

folder=${CM_GIT_CHECKOUT_FOLDER}
if [ ! -d "${CM_TMP_GIT_PATH}" ]; then
  rm -rf ${folder}
  echo "******************************************************"
  echo "Current directory: ${CUR_DIR}"
  echo ""
  echo "Cloning ${CM_GIT_REPO_NAME} from ${CM_GIT_URL}"
  echo ""
  echo "${CM_GIT_CLONE_CMD}";
  echo ""

  ${CM_GIT_CLONE_CMD}
  if [ "${?}" != "0" ]; then exit $?; fi

  cd ${folder}

  if [ ! -z ${CM_GIT_SHA} ]; then

    echo ""
    cmd="git checkout -b ${CM_GIT_SHA} ${CM_GIT_SHA}"
    echo "$cmd"
    eval "$cmd"
    if [ "${?}" != "0" ]; then exit $?; fi

  elif [ ! -z ${CM_GIT_CHECKOUT_TAG} ]; then

    echo ""
    cmd="git fetch --all --tags"
    echo "$cmd"
    eval "$cmd"
    cmd="git checkout tags/${CM_GIT_CHECKOUT_TAG} -b ${CM_GIT_CHECKOUT_TAG}"
    echo "$cmd"
    eval "$cmd"
    if [ "${?}" != "0" ]; then exit $?; fi
  
  else
    cmd="git rev-parse HEAD >> ../tmp-cm-git-hash.out"
    echo "$cmd"
    eval "$cmd"
    if [ "${?}" != "0" ]; then exit $?; fi
  fi

else
  cd ${folder}
fi


IFS=',' read -r -a submodules <<< "${CM_GIT_SUBMODULES}"

for submodule in "${submodules[@]}"
do
    echo ""
    echo "Initializing submodule ${submodule}"
    git submodule update --init "${submodule}"
    if [ "${?}" != "0" ]; then exit $?; fi
done

if [ ${CM_GIT_PATCH} == "yes" ]; then
  IFS=', ' read -r -a patch_files <<< ${CM_GIT_PATCH_FILEPATHS}
  for patch_file in "${patch_files[@]}"
  do
    echo ""
    echo "Applying patch $patch_file"
    git apply "$patch_file"
    if [ "${?}" != "0" ]; then exit $?; fi
  done
fi

cd "$CUR_DIR"
