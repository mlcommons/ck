#!/bin/bash

CUR_DIR=$PWD
echo "$CUR_DIR"
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

folder=${CM_GIT_CHECKOUT_FOLDER}
if [ ! -e "${CM_TMP_GIT_PATH}" ]; then
  cmd="rm -rf ${folder}"
  echo $cmd
  eval $cmd
  echo "******************************************************"
  echo "Current directory: ${CUR_DIR}"
  echo ""
  echo "Cloning ${CM_GIT_REPO_NAME} from ${CM_GIT_URL}"
  echo ""
  echo "${CM_GIT_CLONE_CMD}";
  echo ""

  ${CM_GIT_CLONE_CMD}
  rcode=$?

  if [ ! $rcode -eq 0 ]; then #try once more
    rm -rf $folder
    ${CM_GIT_CLONE_CMD}
    test $? -eq 0 || exit $?
  fi

  cd ${folder}

  if [ ! -z ${CM_GIT_SHA} ]; then

    echo ""
    cmd="git checkout -b ${CM_GIT_SHA} ${CM_GIT_SHA}"
    echo "$cmd"
    eval "$cmd"
    test $? -eq 0 || exit $?

  elif [ ! -z ${CM_GIT_CHECKOUT_TAG} ]; then

    echo ""
    cmd="git fetch --all --tags"
    echo "$cmd"
    eval "$cmd"
    cmd="git checkout tags/${CM_GIT_CHECKOUT_TAG} -b ${CM_GIT_CHECKOUT_TAG}"
    echo "$cmd"
    eval "$cmd"
    test $? -eq 0 || exit $?
  
  else
    cmd="git rev-parse HEAD >> ../tmp-cm-git-hash.out"
    echo "$cmd"
    eval "$cmd"
    test $? -eq 0 || exit $?
  fi

else
  cd ${folder}
fi

if [ ! -z ${CM_GIT_PR_TO_APPLY} ]; then
  echo ""
  echo "Fetching from ${CM_GIT_PR_TO_APPLY}"
  git fetch origin ${CM_GIT_PR_TO_APPLY}:tmp-apply
fi

IFS=',' read -r -a cherrypicks <<< "${CM_GIT_CHERRYPICKS}"
for cherrypick in "${cherrypicks[@]}"
do
  echo ""
  echo "Applying cherrypick $cherrypick"
  git cherry-pick -n $cherrypick
  test $? -eq 0 || exit $?
done

IFS=',' read -r -a submodules <<< "${CM_GIT_SUBMODULES}"

for submodule in "${submodules[@]}"
do
    echo ""
    echo "Initializing submodule ${submodule}"
    git submodule update --init "${submodule}"
    test $? -eq 0 || exit $?
done

if [ ${CM_GIT_PATCH} == "yes" ]; then
  IFS=', ' read -r -a patch_files <<< ${CM_GIT_PATCH_FILEPATHS}
  for patch_file in "${patch_files[@]}"
  do
    echo ""
    echo "Applying patch $patch_file"
    git apply "$patch_file"
    test $? -eq 0 || exit $?
  done
fi

cd "$CUR_DIR"
