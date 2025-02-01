#!/bin/bash

echo "${CM_JAVAC_BIN_WITH_PATH}"
echo ""

${CM_JAVAC_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.java
test $? -eq 0 || exit 1

${CM_JAVA_BIN_WITH_PATH} -classpath "${CM_TMP_CURRENT_SCRIPT_PATH}" code
test $? -eq 0 || exit 1
