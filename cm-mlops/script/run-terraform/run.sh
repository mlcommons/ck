#!/bin/bash
source ${CM_TERRAFORM_CONFIG_DIR}/credentials.sh
source ${CM_TERRAFORM_CONFIG_DIR}/apply_credentials.sh
if [[ $CM_DESTROY_TERRAFORM != "on" ]]; then
  terraform init -input=false
  terraform plan -out=tfplan -input=false
  terraform apply  -input=false tfplan
fi
