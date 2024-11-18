output "vpc_id" {
    value = aws_vpc.main.id
    description = "terraform-vpc ID"
  
}

# output "subnet_id" {
#     value = aws_subnet.public-subnet.id
#      description = "public subnet id"
  
# }
# output "subnet_id" {
#     value = aws_subnet.private-subnet.id
#    description = "private subnet id"
# }