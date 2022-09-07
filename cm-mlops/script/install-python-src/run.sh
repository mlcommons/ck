#!/bin/bash

CUR_DIR=$PWD

echo "***********************************************************"
export PYTHON_VERSION=${CM_VERSION}
CM_WGET_URL="${CM_WGET_URL//"[PYTHON_VERSION]"/$PYTHON_VERSION}"

echo "CM_WGET_URL=${CM_WGET_URL}" >> tmp-run-env.out
echo "wget Python src from ${CM_WGET_URL} for version ${PYTHON_VERSION}..."

CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}

if [[ ${CM_SHARED_BUILD} == "yes" ]]; then
  SHARED_BUILD_FLAGS=" --enable-shared --enable-ssl"
else
  SHARED_BUILD_FLAGS=""
fi
if [[ ${CM_ENABLE_SSL} == "yes" ]]; then
  EXTRA_FLAGS=" --enable-ssl"
else
  EXTRA_FLAGS=""
fi

rm -rf src
mkdir src

rm -rf install
mkdir install

cd src


if [ -f "Python-${PYTHON_VERSION}.tgz" ] ; then
 rm "Python-${PYTHON_VERSION}.tgz"
fi

pwd
wget ${CM_WGET_URL}

if [ "${?}" != "0" ]; then exit 1; fi

tar xzf Python-${PYTHON_VERSION}.tgz
if [ "${?}" != "0" ]; then exit 1; fi


rm -f Python-${PYTHON_VERSION}.tgz
if [ "${?}" != "0" ]; then exit 1; fi

cd Python-${PYTHON_VERSION}

./configure --enable-optimizations ${SHARED_BUILD_FLAGS} ${EXTRA_FLAGS} --with-ensurepip=install --prefix="${CUR_DIR}/install"
if [ "${?}" != "0" ]; then exit 1; fi

make -j${CM_MAKE_CORES} install
if [ "${?}" != "0" ]; then exit 1; fi

cd "${CUR_DIR}" && \
#rm -rf src

if [ "${?}" != "0" ]; then exit 1; fi

cd "${CUR_DIR}/install/bin" && ln -s python3 python

echo "********************************************************"
echo "Python was built and installed to ${CUR_DIR}/install ..."
