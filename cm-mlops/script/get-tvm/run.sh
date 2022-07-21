#!/bin/bash

if [ ! -d "tvm" ]; then
  echo "git clone --recursive -b ${CM_GIT_CHECKOUT} ${CM_GIT_URL} tvm"
  git clone --recursive -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} tvm
  test $? -eq 0 || exit 1
fi

cd tvm 
if [ "${CM_GIT_SHA}" != "" ]; then
  echo "git checkout ${CM_GIT_SHA}"
  git checkout ${CM_GIT_SHA}
  if [ "${?}" != "0" ]; then exit 1; fi
fi

mkdir build

cp cmake/config.cmake build

cd build

if [[ ${CM_TVM_USE_LLVM} == "yes" ]]; then
    sed -i.bak 's/set(USE_LLVM OFF)/set(USE_LLVM ON)/' config.cmake
fi

if [[ ${CM_TVM_USE_OPENMP} == "yes" ]]; then
    sed -i.bak 's/set(USE_OPENMP none)/set(USE_OPENMP gnu)/' config.cmake
fi

cmake ..
test $? -eq 0 || exit 1

make -j4
test $? -eq 0 || exit 1

cd ../../

echo "TVM_HOME=$PWD/tvm" > tmp-run-env.out
