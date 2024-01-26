#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:${PATH}
export ABI=$(python -c "import torch; print(int(torch._C._GLIBCXX_USE_CXX11_ABI))")
mkdir -p llvm-project && cd llvm-project
wget -nc https://github.com/llvm/llvm-project/releases/download/llvmorg-16.0.6/cmake-16.0.6.src.tar.xz
wget -nc https://github.com/llvm/llvm-project/releases/download/llvmorg-16.0.6/llvm-16.0.6.src.tar.xz
tar -xf cmake-16.0.6.src.tar.xz
mv cmake-16.0.6.src cmake
tar -xf llvm-16.0.6.src.tar.xz
mv llvm-16.0.6.src llvm
rm -rf build
mkdir -p build
cd build
export DEB_BUILD_MAINT_OPTIONS=hardening=-format
cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-D_GLIBCXX_USE_CXX11_ABI=${ABI}" -DLLVM_TARGETS_TO_BUILD=X86 -DLLVM_ENABLE_TERMINFO=OFF -DLLVM_INCLUDE_TESTS=OFF -DLLVM_INCLUDE_EXAMPLES=OFF -DLLVM_BUILD_LLVM_DYLIB=ON   -DLLVM_INCLUDE_BENCHMARKS=OFF ../llvm/

cmake --build . -j $(nproc)
export LLVM_ROOT=$CONDA_PREFIX
cmake -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DCMAKE_SHARED_LINKER_FLAGS="-L$CONDA_PREFIX -Wl,-rpath,$CONDA_PREFIX" -P cmake_install.cmake
ln -sf ${LLVM_ROOT}/bin/llvm-config ${LLVM_ROOT}/bin/llvm-config-13 
