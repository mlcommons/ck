#!/bin/bash
if [[ ${CM_TERRAFORM_CONFIG_DIR} == "aws" ]]; then
  source ${CM_TERRAFORM_CONFIG_DIR}/credentials.sh
  source ${CM_TERRAFORM_CONFIG_DIR}/apply_credentials.sh
fi


if [[ -z $CM_DESTROY_TERRAFORM ]]; then
  terraform init -input=false
  terraform plan -out=tfplan -input=false
  terraform apply  -input=false tfplan
  test $? -eq 0 || exit $?
  sleep 20
fi
