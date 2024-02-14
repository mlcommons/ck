#!/bin/bash

rm -rf install
rm -f ${FILENAME}

mkdir -p install

wget --no-check-certificate ${URL}
test $? -eq 0 || exit 1

tar -C install -xzf ${FILENAME}
test $? -eq 0 || exit 1

echo "CM_TMP_INSTALL_FOLDER=$FOLDER" > tmp-run-env.out
