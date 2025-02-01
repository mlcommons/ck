#!/bin/bash

rm -f ${CM_JAVAC_PREBUILT_FILENAME}.tar.gz
rm -f ${CM_JAVAC_PREBUILT_FILENAME}.tar

wget --no-check-certificate ${CM_JAVAC_PREBUILT_URL}${CM_JAVAC_PREBUILT_FILENAME}.tar.gz
test $? -eq 0 || exit 1

gzip -d ${CM_JAVAC_PREBUILT_FILENAME}.tar.gz
test $? -eq 0 || exit 1

tar xvf ${CM_JAVAC_PREBUILT_FILENAME}.tar
test $? -eq 0 || exit 1

rm -f ${CM_JAVAC_PREBUILT_FILENAME}.tar
