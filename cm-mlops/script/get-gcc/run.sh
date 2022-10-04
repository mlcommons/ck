#!/bin/bash
gcc_bin=${CM_GCC_INSTALLED_PATH}/${FILE_NAME_C}
gcc_bin=${CM_GCC_BIN_WITH_PATH:-${gcc_bin}}
echo "${gcc_bin} --version"

${gcc_bin} --version > tmp-ver.out
test $? -eq 0 || exit 1

cat tmp-ver.out
