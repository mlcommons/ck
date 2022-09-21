#!/bin/bash

CUR_DIR=$PWD

code=${CM_MICROTVM_SOURCE}/submissions/tiny_results_v1.0/closed/OctoML/code
model=${CM_TINY_MODEL:-ad}
microtvm_variant=${CM_MICROTVM_VARIANT}
source=${code}/${microtvm_variant}

cd ${ZEPHYR_SDK_INSTALL_DIR}
west update
west zephyr-export

cd ${source}/NUCLEO_L4R5ZI/${model}
rm -rf build
mkdir -p build
cd build
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES:-2}}
cmake ..
make -j${CM_MAKE_CORES}
