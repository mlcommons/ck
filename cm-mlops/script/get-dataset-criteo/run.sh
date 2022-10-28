#!/bin/bash

if [ -n ${CM_CRITEO_PATH} ]; then
  echo "CM_DATASET_PATH=${CRITEO_PATH}" > tmp-run-env.out
  exit 0
fi

curl -O -C - https://storage.googleapis.com/criteo-cail-datasets/day_{`seq -s "," 0 23`}.gz
test $? -eq 0 || exit 1

if [ ${CM_COPY_ZIP_FILES} == "yes" ]; then
    mkdir backup
    cp -r *.gz backup/
fi
gunzip day_{0..23}.gz
echo "CM_DATASET_PATH=$PWD" > tmp-run-env.out
