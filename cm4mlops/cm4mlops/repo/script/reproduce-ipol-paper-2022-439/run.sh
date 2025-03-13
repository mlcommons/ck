#!/bin/bash

echo "======================================================="

CUR_DIR=${PWD}
echo "Current path in CM script: ${CUR_DIR}"

echo ""
echo "Installing extra requirements (latest versions) ..."

echo ""
${CM_PYTHON_BIN_WITH_PATH} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt

echo "======================================================="

cd ${CM_IPOL_PATH}

echo "Current path in CM cache: ${PWD}"

# Check default images
if [ "${CM_INPUT_1}" == "" ]; then
  CM_INPUT_1=${CM_TMP_CURRENT_SCRIPT_PATH}/sample-images/1.png
fi

if [ "${CM_INPUT_2}" == "" ]; then
  CM_INPUT_2=${CM_TMP_CURRENT_SCRIPT_PATH}/sample-images/2.png
fi

echo "Running author's code ..."

rm -f cm.png
rm -f ${CUR_DIR}/diff.png

echo ""
${CM_PYTHON_BIN_WITH_PATH} main.py --input_0=${CM_INPUT_1}  --input_1=${CM_INPUT_2}
test $? -eq 0 || exit 1

# Copy diff png to current path
cp cm.png ${CUR_DIR}/diff.png
test $? -eq 0 || exit 1

echo "======================================================="
