#!/bin/bash

echo ""
echo "Unarchiving ${CM_CMAKE_PACKAGE} ..."

tar --strip 1 -xf ${CM_CMAKE_PACKAGE}
test $? -eq 0 || exit 1

rm -f ${CM_CMAKE_PACKAGE}
test $? -eq 0 || exit 1
