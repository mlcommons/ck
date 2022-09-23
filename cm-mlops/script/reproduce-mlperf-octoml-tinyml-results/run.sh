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

path_suffix="NUCLEO_L4R5ZI/${model}"
cmake_src=${source}/${path_suffix}
build_path=${CUR_DIR}/${path_suffix}
mkdir -p ${build_path}
cd ${build_path}
binary_path=${build_path}/build/zephyr/zephyr.elf
if [ -f ${binary_path} ] and [ ${CM_RECREATE_BINARY} != "yes" ]; then
  echo "ELF binary existing at ${binary_path}. Skipping regeneration."
  cd build
else
  rm -rf build
  mkdir -p build
  cd build
  CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES:-2}}
  cmake ${cmake_src}
  test $? -eq 0 || exit 1
  make -j${CM_MAKE_CORES}
  test $? -eq 0 || exit 1
  cd ../
  echo "ELF binary created at ${build_path}/build/zephyr/zephyr.elf"
fi
if [[ ${CM_FLASH_BOARD} == "yes" ]]; then
  west flash
  test $? -eq 0 || exit 1
fi
