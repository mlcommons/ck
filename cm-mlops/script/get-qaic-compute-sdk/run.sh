#!/bin/bash
wget https://codelinaro.jfrog.io/artifactory/codelinaro-toolchain-for-hexagon/v15.0.5/clang+llvm-15.0.5-cross-hexagon-unknown-linux-musl.tar.xz
export HEXAGON_TOOLS_DIR=`pwd`/clang+llvm-15.0.5-cross-hexagon-unknown-linux-musl/x86_64-linux-gnu
cd ${CM_QAIC_COMPUTE_SDK_PATH}
./scripts/build.sh --release --install
test $? -eq 0 || exit $?
