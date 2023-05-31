#!/bin/bash

echo ""

wget -4 -nc ${CM_WGET_URL} --no-check-certificate
test $? -eq 0 || exit 1

mkdir data

tar -C data -xvzf caffe_ilsvrc12.tar.gz
test $? -eq 0 || exit 1

rm -rf caffe_ilsvrc12.tar.gz

echo "CM_DATASET_AUX_PATH=$PWD/data" > tmp-run-env.out
