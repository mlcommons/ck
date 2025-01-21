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
mkdir -p train_data/train
mkdir -p train_data/val
rsync -avz ${CM_DATASET_IMAGENET_TRAIN_PATH}/ train_data/train/
rsync -avz ${CM_DATASET_IMAGENET_VAL_PATH}/ train_data/val/
cd train_data/train
find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done
cd ../val
run "wget  --no-check-certificate -qO- https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh | bash"
cd ../../
DATA_DIR=`pwd`/train_data

CUR=${CM_DATA_DIR}
run "cd \"${CM_RUN_DIR}\""
run "docker build --build-arg FROM_IMAGE_NAME=nvcr.io/nvidia/mxnet:${MXNET_VER}-py3 -t nvidia_rn50_mx ."
run "ID=`docker run -dt --gpus all --runtime=nvidia --ipc=host -v ${DATA_DIR}:/data -v ${CUR}:/preprocessed nvidia_rn50_mx bash`"
run "docker exec $ID bash -c './scripts/prepare_imagenet.sh /data /preprocessed'"
