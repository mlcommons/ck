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
}

