#!/bin/bash

which ${CM_JAVA_BIN_WITH_PATH}

${CM_JAVA_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.java
test $? -eq 0 || exit $?
