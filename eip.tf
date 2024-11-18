resource "aws_eip" "nat-gw-ip" {
  domain   = "vpc"
}