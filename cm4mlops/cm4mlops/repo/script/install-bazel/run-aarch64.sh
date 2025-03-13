#!/bin/bash

CUR_DIR=$PWD
echo "******************************************************"

CM_WGET_URL=${CM_WGET_URL//"[OS]"/${CM_HOST_OS_TYPE}}
CM_WGET_URL=${CM_WGET_URL//"[PLATFORM]"/arm64}
CM_WGET_URL=${CM_WGET_URL//"[VERSION]"/${CM_VERSION}}
CM_WGET_URL=${CM_WGET_URL//"-installer-"/-}
CM_WGET_URL=${CM_WGET_URL//".sh"/}
echo "CM_WGET_URL=${CM_WGET_URL}" > tmp-run-env.out
BAZEL_SCRIPT="bazel-${CM_VERSION}-${CM_HOST_OS_TYPE}-arm64"

INSTALL_DIR=${CUR_DIR}
rm -rf ${INSTALL_DIR}/bin
wget -c ${CM_WGET_URL}
if [ "${?}" != "0" ]; then exit 1; fi
chmod +x ${BAZEL_SCRIPT}
ln -s ${BAZEL_SCRIPT} bazel
if [ "${?}" != "0" ]; then exit 1; fi

echo "CM_BAZEL_INSTALLED_PATH=${INSTALL_DIR}" >>tmp-run-env.out
echo "CM_BAZEL_BIN_WITH_PATH=${INSTALL_DIR}/${BAZEL_SCRIPT}" >>tmp-run-env.out

echo "Bazel is installed to ${INSTALL_DIR} ..."
