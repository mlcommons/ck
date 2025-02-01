#!/bin/bash

CUR_DIR=${PWD:-tmp}
if [ ! -d "src" ]; then
  echo "Cloning Tensorflow from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT} --depth ${CM_GIT_DEPTH}..."
  git clone --recursive -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} --depth ${CM_GIT_DEPTH} src
fi

INSTALL_DIR="${CUR_DIR}"
rm -rf ${INSTALL_DIR}/build

cd ${INSTALL_DIR}
mkdir -p build
mkdir -p install

echo "******************************************************"
cd build
cmake ../src/tensorflow/lite/c
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
cmake --build . -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi


echo "******************************************************"
echo "Tflite is built to ${INSTALL_DIR}/build ..."
