#!/bin/bash

function cmake() {
${CM_CMAKE_BIN_WITH_PATH} $@
}

export CC=${CM_C_COMPILER_WITH_PATH}
export CXX=${CM_CXX_COMPILER_WITH_PATH}

export -f cmake
export HEXAGON_TOOLS_DIR=${CM_HEXAGON_TOOLS_INSTALLED_DIR}/clang+llvm-15.0.5-cross-hexagon-unknown-linux-musl/x86_64-linux-gnu

mkdir -p src
rsync -avz --exclude=.git  ${CM_QAIC_COMPUTE_SDK_PATH}/ src/
cd src

if [[ ${CM_CLEAN_BUILD} == "yes" ]]; then
  rm -rf build
fi

./scripts/build.sh --${CM_QAIC_COMPUTE_SDK_INSTALL_MODE} --install
test $? -eq 0 || exit $?

cd -
