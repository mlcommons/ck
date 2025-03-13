#!/bin/bash

CUR_DIR=${PWD}
SPEC_EXP_ROOT=${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment
SPEC_INSTALL=${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment/spec
SPEC_MNT=${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment/spec_mnt

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo ""
echo "SPEC ISO PATH:${SPEC_ISO}"
echo "Installing to ${SPEC_INSTALL}"

mkdir -p ${SPEC_MNT}
test $? -eq 0 || exit 1

mkdir -p ${SPEC_INSTALL}
test $? -eq 0 || exit 1

sudo mount -t iso9660 -o ro,exec,loop /path/to/cpu2017-1_0_5.iso ${CUR_DIR}/spec_mnt
test $? -eq 0 || exit 1

cd ${SPEC_MNT}
./install.sh -d ${SPEC_INSTALL}
test $? -eq 0 || exit 1

cp ${CM_GIT_REPO_XFM_CHECKOUT_PATH}/spec_workload_experiment/config/default.cfg ${SPEC_INSTALL}/config
test $? -eq 0 || exit 1

cd ${SPEC_EXP_ROOT}
./fetch_corpus.sh
test $? -eq 0 || exit 1
cd lzbench
make -j BUILD_STATIC=1
test $? -eq 0 || exit 1