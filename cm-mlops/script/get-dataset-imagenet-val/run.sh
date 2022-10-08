#!/bin/bash

if [ ${CM_IMAGENET_FULL:-no} == "yes" ]; then
  if [ -z ${IMAGENET_PATH} ]; then
    echo "Please set IMAGENET_PATH to the folder containing full imagenet images"
    exit 1
  fi
  echo "CM_DATASET_PATH=${IMAGENET_PATH}" > tmp-run-env.out
  exit 0
fi

test $? -eq 0 || exit 1

if [ -f "ILSVRC2012_img_val_500.tar" ]; then
  rm -f ILSVRC2012_img_val_500.tar
fi
test $? -eq 0 || exit 1

wget -nc https://www.dropbox.com/s/57s11df6pts3z69/ILSVRC2012_img_val_500.tar --no-check-certificate
test $? -eq 0 || exit 1

if [ -d "images" ]; then
  rm -rf images
fi

mkdir images

tar -C images -xvf ILSVRC2012_img_val_500.tar
test $? -eq 0 || exit 1

rm -rf ILSVRC2012_img_val_500.tar

echo "CM_DATASET_PATH=$PWD/images" > tmp-run-env.out
