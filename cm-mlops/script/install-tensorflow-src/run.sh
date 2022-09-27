#!/bin/bash

CUR_DIR=${PWD:-tmp}
if [ ! -d "src" ]; then
  echo "Cloning Tensorflow from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."
  git clone --recursive -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} src
fi
CM_PYTHON_BIN=${CM_PYTHON_BIN:-python3}
${CM_PYTHON_BIN} -m pip install numpy
test $? -eq 0 || exit 1

INSTALL_DIR="${CUR_DIR}"
rm -rf ${INSTALL_DIR}/install

cd ${INSTALL_DIR}
mkdir -p build
mkdir -p install

echo "******************************************************"
cd src
./configure
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
bazel build //tensorflow/tools/pip_package:build_pip_package
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
if [ "${?}" != "0" ]; then exit 1; fi


# Clean build directory (too large)
cd ${INSTALL_DIR}
if [ "${CM_TENSORFLOW_CLEAN_BUILD}" != "no" ]; then
    rm -rf build
fi

echo "******************************************************"
echo "Tensorflow is built and installed to ${INSTALL_DIR}/install ..."
