#!/bin/bash

CUR_DIR=${PWD:-tmp}
if [ ! -d "src" ]; then
  echo "Cloning Tensorflow from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."
  git clone --recursive -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} src
fi

INSTALL_DIR="${CUR_DIR}"
rm -rf ${INSTALL_DIR}/install

cd ${INSTALL_DIR}
mkdir -p build
mkdir -p install

echo "******************************************************"
cd build
cmake ../src/tensorflow/lite
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
cmake --build . -j
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory
cd ${INSTALL_DIR}
if [ "${CM_TFLITE_CLEAN_BUILD}" != "no" ]; then
    rm -rf build
fi

echo "******************************************************"
echo "Tflite is built and installed to ${INSTALL_DIR}/install ..."
