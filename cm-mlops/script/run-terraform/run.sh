#!/bin/bash
source ${CM_TERRAFORM_CONFIG_DIR}/credentials.sh
source ${CM_TERRAFORM_CONFIG_DIR}/apply_credentials.sh
terraform init -input=false
terraform plan -out=tfplan -input=false
terraform apply  -input=false tfplan
