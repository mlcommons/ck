#!/bin/bash

if [ "${CM_DATASET_PATH}" == "" ]; then

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
  echo "CM_DATASET_IMAGENET_PATH=$PWD/images" > tmp-run-env.out

fi
