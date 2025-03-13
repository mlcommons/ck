#!/bin/bash

CUR_DIR=$PWD

echo "***********************************************************"
export PYTHON_VERSION=${CM_VERSION}
CM_WGET_URL="${CM_WGET_URL//"[PYTHON_VERSION]"/$PYTHON_VERSION}"

echo "CM_WGET_URL=${CM_WGET_URL}" >> tmp-run-env.out
echo "wget Python src from ${CM_WGET_URL} for version ${PYTHON_VERSION}..."

CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

if [[ ${CM_SHARED_BUILD} == "yes" ]]; then
  SHARED_BUILD_FLAGS=" --enable-shared"
else
  SHARED_BUILD_FLAGS=""
fi

EXTRA_FLAGS=""

if [[ ${CM_ENABLE_SSL} == "yes" ]]; then
  EXTRA_FLAGS="${EXTRA_FLAGS} --enable-ssl"
fi


if [[ ${CM_CUSTOM_SSL} == "yes" ]]; then
  EXTRA_FLAGS="${EXTRA_FLAGS} --with-openssl=${CM_OPENSSL_INSTALLED_PATH} --with-openssl-rpath=auto"
fi

rm -rf src
mkdir src

rm -rf install
mkdir install

cd src

pwd
wget -nc ${CM_WGET_URL}

if [ "${?}" != "0" ]; then exit 1; fi

tar xzf Python-${PYTHON_VERSION}.tgz
if [ "${?}" != "0" ]; then exit 1; fi


rm -f Python-${PYTHON_VERSION}.tgz
if [ "${?}" != "0" ]; then exit 1; fi

cd Python-${PYTHON_VERSION}

./configure ${CM_PYTHON_OPTIMIZATION_FLAG} ${CM_PYTHON_LTO_FLAG} ${SHARED_BUILD_FLAGS} ${EXTRA_FLAGS} --with-ensurepip=install --prefix="${CUR_DIR}/install"
if [ "${?}" != "0" ]; then exit 1; fi

make -j${CM_MAKE_CORES}
make -j${CM_MAKE_CORES} install
if [ "${?}" != "0" ]; then exit 1; fi

echo "Removing src files"
cd "${CUR_DIR}" && \
rm -rf src

if [ "${?}" != "0" ]; then exit 1; fi

cd "${CUR_DIR}/install/bin" && ln -s python3 python
cd "${CUR_DIR}/install/bin" && ln -s pip3 pip

echo "********************************************************"
echo "Python was built and installed to ${CUR_DIR}/install ..."
