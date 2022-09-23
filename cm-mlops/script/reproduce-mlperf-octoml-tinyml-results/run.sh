#!/bin/bash

CUR_DIR=$PWD

code=${CM_MICROTVM_SOURCE}/submissions/tiny_results_v1.0/closed/OctoML/code
model=${CM_TINY_MODEL:-ad}
microtvm_variant=${CM_MICROTVM_VARIANT}
source=${code}/${microtvm_variant}

cd ${CM_ZEPHYR_DIR}
west update
test $? -eq 0 || exit 1
west zephyr-export

cmake_src=${source}/NUCLEO_L4R5ZI/${model}
cd ${CUR_DIR}
rm -rf build
mkdir -p build
cd build
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES:-2}}
cmake ${cmake_src}
test $? -eq 0 || exit 1
make -j${CM_MAKE_CORES}
test $? -eq 0 || exit 1
cd ../
echo "ELF binary created at $CUR/build/zephyr/zephyr.elf"
if [[ ${CM_FLASH_BOARD} == "yes" ]]; then
  west flash
  test $? -eq 0 || exit 1
fi
