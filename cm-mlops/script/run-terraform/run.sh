#!/bin/bash
source ${CM_TERRAFORM_CONFIG_DIR}/credentials.sh
source ${CM_TERRAFORM_CONFIG_DIR}/apply_credentials.sh
if [[ -z $CM_DESTROY_TERRAFORM ]]; then
  terraform init -input=false
  terraform plan -out=tfplan -input=false
  terraform apply  -input=false tfplan
  test $? -eq 0 || exit 1
  sleep 20
fi
