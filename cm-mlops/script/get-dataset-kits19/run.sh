#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

echo "******************************************************"
echo "Cloning kits19 from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} ${CM_GIT_DEPTH} ${CM_GIT_RECURSE_SUBMODULES}..."

if [ ! -d "kits19" ]; then
  if [ -z ${CM_GIT_SHA} ]; then
    cmd="git clone ${CM_GIT_RECURSE_SUBMODULES} -b ${CM_GIT_CHECKOUT} ${CM_GIT_URL} ${CM_GIT_DEPTH} kits19"
    echo $cmd
    eval $cmd
    cd kits19
  else
    git clone ${CM_GIT_RECURSE_SUBMODULES} ${CM_GIT_URL} ${CM_GIT_DEPTH} kits19
    cd kits19
    git checkout -b "${CM_GIT_CHECKOUT}"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi
else
  cd kits19
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
cd ${CUR_DIR}/kits19
${CM_PYTHON_BIN_WITH_PATH} -m starter_code.get_imaging
cd data
cp -rf case_00185 case_00400
cd "$CUR_DIR"
