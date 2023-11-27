#!/bin/bash

CUR_DIR=$PWD

mkdir -p install
mkdir -p build

INSTALL_DIR="${CUR_DIR}/install"

echo "******************************************************"

cd build

if [ "${CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD}" == "YES" ]; then
    export CM_MLPERF_INFERENCE_SOURCE="${CM_EXTRACT_EXTRACTED_PATH}"
fi


if [ -z "${CM_MLPERF_INFERENCE_SOURCE}" ]; then
   echo "Error: env CM_MLPERF_INFERENCE_SOURCE is not defined - something is wrong with script automation!"
   exit 1
fi

cmake \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}" \
     "${CM_MLPERF_INFERENCE_SOURCE}/loadgen" \
     -DPYTHON_EXECUTABLE:FILEPATH=${CM_PYTHON_BIN_WITH_PATH}
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j ${CM_MAKE_CORES}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean build directory (too large)
cd "${CUR_DIR}"
rm -rf build

PYTHON_VERSION=`${CM_PYTHON_BIN_WITH_PATH} -V |cut -d' ' -f2`
PYTHON_SHORT_VERSION=${PYTHON_VERSION%.*}
PYTHON_MINOR_VERSION=${PYTHON_SHORT_VERSION#*.}
MLPERF_INFERENCE_PYTHON_SITE_BASE=${INSTALL_DIR}"/python"

cd "${CM_MLPERF_INFERENCE_SOURCE}/loadgen"
CFLAGS="-std=c++14 -O3" ${CM_PYTHON_BIN_WITH_PATH} setup.py bdist_wheel
${CM_PYTHON_BIN_WITH_PATH} -m pip install --force-reinstall `ls dist/mlperf_loadgen-*cp3${PYTHON_MINOR_VERSION}*.whl` --target=${MLPERF_INFERENCE_PYTHON_SITE_BASE}
if [ "${?}" != "0" ]; then exit 1; fi

# Clean the built wheel
find . -name 'mlperf_loadgen*.whl' | xargs rm

echo "******************************************************"
echo "Loadgen is built and installed to ${INSTALL_DIR} ..."
