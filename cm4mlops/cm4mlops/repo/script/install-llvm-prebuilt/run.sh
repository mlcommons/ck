#!/bin/bash

echo ""
echo "Unarchiving ${CM_LLVM_PACKAGE} ..."

tar --strip 1 -xf ${CM_LLVM_PACKAGE}
test $? -eq 0 || exit 1

rm -f ${CM_LLVM_PACKAGE}
test $? -eq 0 || exit 1
