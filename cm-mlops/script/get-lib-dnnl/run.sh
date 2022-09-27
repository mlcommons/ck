#!/bin/bash

CUR_DIR=${PWD:-tmp}

git clone --recursive -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} src

test $? -eq 0 || exit 1

INSTALL_DIR="${CUR_DIR}"
rm -rf ${INSTALL_DIR}/install

cd ${INSTALL_DIR}
mkdir build
mkdir install

echo "******************************************************"
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_DIR}/install" \
    -DCMAKE_BUILD_TYPE=Release \
    -DDNNL_BUILD_TESTS=${DNNL_BUILD_TESTS} \
    -DDNNL_BUILD_EXAMPLES=${DNNL_BUILD_EXAMPLES} \
    -DDNNL_CPU_RUNTIME=${DNNL_CPU_RUNTIME} \
    ../src/
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
cmake --build . -j${CM_CPUINFO_CPUs}
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
cmake --install .
if [ "${?}" != "0" ]; then exit 1; fi


# Clean build directory (too large)
cd ${INSTALL_DIR}
if [ "${CM_DNNL_CLEAN_BUILD}" != "no" ]; then
    rm -rf build
fi

echo "******************************************************"
echo "DNNL was built and installed to ${INSTALL_DIR}/install ..."
