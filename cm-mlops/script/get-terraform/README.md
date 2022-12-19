# Get Terraform
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) detects the installed Terraform on the system and if not found calls the [install script for Terraform](../script/install-terraform-from-src).

## Exported Variables
* `CM_TERRAFORM_BIN_WITH_PATH`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
