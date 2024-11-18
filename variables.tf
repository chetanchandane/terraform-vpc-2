variable "aws_access_key" {  }
variable "aws_secret_key" {  }
# to store the keys I am going to use the export command.

variable "vpc_cidr_block" {
    description = "CIDR block for terraform-vpc"
    type = string
    default = "10.0.0.0/16"
}

