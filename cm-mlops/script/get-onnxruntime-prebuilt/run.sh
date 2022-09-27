#!/bin/bash

CM_VERSION=${CM_VERSION:-1.12.1}

mkdir -p install
machine=${CM_HOST_OS_MACHINE:-x86_64}
if [[ $machine == "x86_64" ]]; then
  machine=x64
fi
hostos=${CM_HOST_OS_TYPE}
if [[ $hostos == "darwin" ]]; then
  hostos=osx
fi

FOLDER=onnxruntime-${hostos}-$machine-${CM_VERSION}
FILENAME=$FOLDER".tgz"
WGET_CMD="-q --no-check-certificate https://github.com/microsoft/onnxruntime/releases/download/v${CM_VERSION}/${FILENAME}"
echo "wget ${WGET_CMD}"
wget ${WGET_CMD}
test $? -eq 0 || exit 1
tar -C install -xzf ${FILENAME}
test $? -eq 0 || exit 1
echo "CM_TMP_INSTALL_FOLDER=$FOLDER" > tmp-run-env.out

