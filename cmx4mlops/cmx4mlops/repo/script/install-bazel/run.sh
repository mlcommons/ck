#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"

CM_WGET_URL=${CM_WGET_URL//"[OS]"/${CM_HOST_OS_TYPE}}
CM_WGET_URL=${CM_WGET_URL//"[PLATFORM]"/${CM_HOST_PLATFORM_FLAVOR}}
CM_WGET_URL=${CM_WGET_URL//"[VERSION]"/${CM_VERSION}}

echo "CM_WGET_URL=${CM_WGET_URL}" >> tmp-run-env.out

BAZEL_SCRIPT="bazel-${CM_VERSION}-installer-${CM_HOST_OS_TYPE}-${CM_HOST_PLATFORM_FLAVOR}.sh"

INSTALL_DIR=${CUR_DIR}

rm -rf ${INSTALL_DIR}/bin

wget -c ${CM_WGET_URL} --no-check-certificate

if [ "${?}" != "0" ]; then exit 1; fi

chmod +x ${BAZEL_SCRIPT}

./${BAZEL_SCRIPT} --bin=${INSTALL_DIR}"/bin" --base=${INSTALL_DIR}"/install"
if [ "${?}" != "0" ]; then exit 1; fi

echo "Bazel is installed to ${INSTALL_DIR} ..."
