#!/bin/bash

CUR_DIR=$PWD

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

cmake \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
     "${CM_MLC_INFERENCE_SOURCE}/loadgen"
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd "${CUR_DIR}"
rm -rf build

${CM_PYTHON_BIN} -m pip install wheel
PYTHON_VERSION=`${CM_PYTHON_BIN} -V |cut -d' ' -f2`
PYTHON_SHORT_VERSION=${PYTHON_VERSION%.*}
MLC_INFERENCE_PYTHON_SITE_BASE=${INSTALL_DIR}"/python"

cd "${CM_MLC_INFERENCE_SOURCE}/loadgen"
CFLAGS="-std=c++14 -O3" ${CM_PYTHON_BIN} setup.py bdist_wheel
${CM_PYTHON_BIN} -m pip install --force-reinstall `ls dist/mlperf_loadgen*.whl` --target="${MLC_INFERENCE_PYTHON_SITE_BASE}"
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
echo "Loadgen is built and installed to ${INSTALL_DIR} ..."
