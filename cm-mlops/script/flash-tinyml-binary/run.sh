#!/bin/bash

build_dir=${CM_TINY_BINARY_DIR}
cd ${CM_ZEPHYR_DIR}
west flash --build-dir ${build_dir}
test $? -eq 0 || exit 1

