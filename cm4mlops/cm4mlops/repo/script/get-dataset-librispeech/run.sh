#!/bin/bash

wget -nc ${CM_WGET_URL} --no-check-certificate
test $? -eq 0 || exit 1

tar -x --skip-old-files -vf ${CM_DATASET_ARCHIVE}
test $? -eq 0 || exit 1

