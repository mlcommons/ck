#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"
echo "Cloning Mlcommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "inference" ]; then
  git clone --recurse-submodules -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} inference
  if [ "${?}" != "0" ]; then exit 1; fi
fi

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

cmake \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
    ../inference/loadgen
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_NUMBER_OF_PROCESSORS}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd ${CUR_DIR}
rm -rf build

${CM_PYTHON_BIN} -m pip install wheel
PYTHON_VERSION=`${CM_PYTHON_BIN} -V |cut -d' ' -f2`
PYTHON_SHORT_VERSION=${PYTHON_VERSION%.*}
MLC_INFERENCE_PYTHON_SITE_BASE=${INSTALL_DIR}"/python"
MLC_INFERENCE_PYTHON_SITE=${MLC_INFERENCE_PYTHON_SITE_BASE}"/lib/python${PYTHON_SHORT_VERSION}/site-packages"
echo "PYTHONPATH=$PYTHONPATH:${MLC_INFERENCE_PYTHON_SITE}" >> tmp-run-env.out

cd inference/loadgen
CFLAGS="-std=c++14 -O3" ${CM_PYTHON_BIN} setup.py bdist_wheel
${CM_PYTHON_BIN} -m pip install --force-reinstall `ls dist/mlperf_loadgen*.whl` --prefix=${MLC_INFERENCE_PYTHON_SITE_BASE}
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
echo "Loadgen is built and installed to ${INSTALL_DIR} ..."
