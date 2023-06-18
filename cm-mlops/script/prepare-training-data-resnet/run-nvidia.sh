#!/bin/bash

#CM Script location: ${CM_TMP_CURRENT_SCRIPT_PATH}

#To export any variable
#echo "VARIABLE_NAME=VARIABLE_VALUE" >>tmp-run-env.out

#${CM_PYTHON_BIN_WITH_PATH} contains the path to python binary if "get,python" is added as a dependency



function exit_if_error() {
  test $? -eq 0 || exit $?
}

function run() {
  echo "Running: "
  echo "$1"
  echo ""
  if [[ ${CM_FAKE_RUN} != 'yes' ]]; then
    eval "$1"
    exit_if_error
  fi
}

#Add your run commands here...
# run "$CM_RUN_CMD"
CUR=${CM_DATA_DIR:-"$PWD/data"}
run "cd \"${CM_RUN_DIR}\""
run "docker build -t nvidia_rn50_mx ."
run "ID=`docker run -dt --gpus all --runtime=nvidia --ipc=host -v ${CM_DATASET_IMAGENET_TRAIN_PATH}:/data -v ${CUR}:/preprocessed nvidia_rn50_mx bash`"
run "docker exec $ID bash -c './scripts/prepare_imagenet.sh /data /preprocessed'"
