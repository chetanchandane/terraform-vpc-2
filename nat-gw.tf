resource "aws_nat_gateway" "NAT" {
  allocation_id = aws_eip.nat-gw-ip.id
  subnet_id     = aws_subnet.public-subnet.id

  tags = {
    Name = "NAT-gateway"
  }

}