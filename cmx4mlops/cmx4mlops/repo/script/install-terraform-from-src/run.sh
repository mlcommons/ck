#!/bin/bash

CUR_DIR=${PWD}
if [ ! -d "terraform" ]; then
  echo "Cloning Terraform from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."
  git clone  -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} terraform
fi
test $? -eq 0 || exit 1

export GOPATH=$CUR_DIR
cd terraform
go install
test $? -eq 0 || exit 1

echo "******************************************************"
echo "Terraform is built and installed to ${GOPATH}/bin/terraform ..."
