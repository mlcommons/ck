variable ACCESS_KEY {
  type = string
  description = "AWS access key"
}
variable SECRET_KEY {
  type = string
  description = "AWS secret key"
}
variable TOKEN {
  type = string
  description = "AWS Token"
}
variable INSTANCE_TYPE {
  type = string
  description = "AWS instance type"
}
variable SECURITY_GROUP_ID {
  type = string
  description = "AWS instance security group id"
}
variable CPU_COUNT {
  default = 1
  description = "AWS CPU count"
}
variable DISK_GBS {
  default = 8
  description = "AWS Disk space in GBs"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
  access_key=var.ACCESS_KEY
  secret_key=var.SECRET_KEY
  token=var.TOKEN
}

resource "aws_instance" "cm" {
  ami                       = "ami-017fecd1353bcc96e"
  instance_initiated_shutdown_behavior = "terminate"
  instance_type           = var.INSTANCE_TYPE
  key_name = "cmuser"
  vpc_security_group_ids = [
    var.SECURITY_GROUP_ID
  ]
  root_block_device {
    delete_on_termination = true
    volume_size           = var.DISK_GBS
  }
}

