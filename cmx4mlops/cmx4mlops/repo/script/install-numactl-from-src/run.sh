#!/bin/bash

CUR_DIR=$PWD
echo $PWD
rm -rf numactl
cmd="cp -r ${CM_NUMACTL_SRC_REPO_PATH} numactl"
echo "$cmd"
eval "$cmd"
cd numactl
./autogen.sh
./configure
if [ "${?}" != "0" ]; then exit 1; fi
make
if [ "${?}" != "0" ]; then exit 1; fi
#make install DESTDIR=$CUR_DIR
sudo make install
if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
