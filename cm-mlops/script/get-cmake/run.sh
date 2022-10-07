#!/bin/bash
cmake_bin=${CM_CMAKE_BIN_WITH_PATH}

${cmake_bin} --version > tmp-ver.out
test $? -eq 0 || exit 1
