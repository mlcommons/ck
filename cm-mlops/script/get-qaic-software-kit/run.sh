#!/bin/bash

cd ${CM_QAIC_SOFTWARE_KIT_PATH}
./bootstrap.sh
test $? -eq 0 || exit $?
cd build
../scripts/build.sh -b Release
test $? -eq 0 || exit $?
