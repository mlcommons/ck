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
     -DPYTHON_EXECUTABLE:FILEPATH="${CM_PYTHON_BIN_WITH_PATH}" -B .
if [ ${?} -ne 0 ]; then exit $?; fi

echo "******************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

cmake --build . --target install -j "${CM_MAKE_CORES}"
if [ ${?} -ne 0 ]; then exit $?; fi

# Clean build directory (too large)
cd "${CUR_DIR}"
if [[ $CM_MLPERF_INFERENCE_LOADGEN_BUILD_CLEAN == "yes" ]]; then
  rm -rf build
fi


cd "${CM_MLPERF_INFERENCE_SOURCE}/loadgen"
${CM_PYTHON_BIN_WITH_PATH} -m pip install . --target="${MLPERF_INFERENCE_PYTHON_SITE_BASE}"

if [ ${?} -ne 0 ]; then exit $?; fi

# Clean the built wheel
#find . -name 'mlcommons_loadgen*.whl' | xargs rm

echo "******************************************************"
echo "Loadgen is built and installed to ${INSTALL_DIR} ..."
