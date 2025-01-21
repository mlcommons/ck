#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsEvaluation/


cd A-riscv/

git clone https://github.com/riscv-collab/riscv-gnu-toolchain
cd riscv-gnu-toolchain/
git checkout 2022.01.17
CFLAGS="-O2 -static" ./configure --prefix=$(realpath ../riscv_gcc111) --with-arch=rv64g
make linux -j$(nproc)
make -j$(nproc)
cd ../

cd musl/
CC=../riscv_gcc111/bin/riscv64-unknown-linux-gnu-gcc CROSS_COMPILE=../riscv_gcc111/bin/riscv64-unknown-linux-gnu- ./configure --prefix=$(realpath ../musl-gcc) --target=riscv64
make -j$(nproc)
make install
cd ../../

wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-16.04.tar.xz
tar xf clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-16.04.tar.xz
mv clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu- clang+llvm-12.0.1-x86_64-linux-gnu-ubuntu-16.04
