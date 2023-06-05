#!/bin/bash

wget -nc ${CM_DATASET_CIFAR10} --no-check-certificate
test $? -eq 0 || exit 1

rm -rf ${CM_DATASET_FILENAME1}

gzip -d ${CM_DATASET_FILENAME}
test $? -eq 0 || exit 1

tar -xvf ${CM_DATASET_FILENAME1}
test $? -eq 0 || exit 1

rm -rf ${CM_DATASET_FILENAME}

echo "CM_DATASET_PATH=$PWD/cifar-10-batches-py" > tmp-run-env.out
echo "CM_DATASET_CIFAR10_PATH=$PWD/cifar-10-batches-py" >> tmp-run-env.out
