#!/bin/bash

CUR_DIR=${PWD:-tmp}

wget -nc ${CM_LIB_ARMNN_PREBUILT_BINARY_URL}
tar -xvzf ${CM_LIB_ARMNN_EXTRACT_FILENAME}

echo "******************************************************"
echo "ArmNN prebuilt binary downloaded to ${CUR_DIR} ..."
