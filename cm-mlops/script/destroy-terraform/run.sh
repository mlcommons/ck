#!/bin/bash
source ${CM_TERRAFORM_CONFIG_DIR}/credentials.sh
source ${CM_TERRAFORM_CONFIG_DIR}/apply_credentials.sh
cd ${CM_TERRAFORM_RUN_DIR}
terraform destroy --auto-approve
test $? -eq 0 || exit 1
