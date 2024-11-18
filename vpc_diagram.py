from diagrams import Diagram, Edge
from diagrams.aws.network import VPC, InternetGateway, NATGateway, PublicSubnet, PrivateSubnet, RouteTable
from diagrams.aws.general import InternetAlt1

with Diagram("AWS VPC Infrastructure", show=False, direction="TB"):
    internet = InternetAlt1("Internet")
    
    with VPC("VPC (10.0.0.0/16)") as vpc:
        igw = InternetGateway("Internet Gateway")
        
        with (public_cluster := PublicSubnet("Public Subnet\n10.0.1.0/24")):
            nat = NATGateway("NAT Gateway")
            public_rt = RouteTable("Public Route Table")
        
        with (private_cluster := PrivateSubnet("Private Subnet\n10.0.2.0/24")):
            private_rt = RouteTable("Private Route Table")
    
    internet >> Edge(color="orange", style="dashed") >> igw
    igw >> Edge(color="orange") >> public_cluster
    public_cluster >> Edge(color="orange") >> nat
    nat >> Edge(color="red", style="dashed") >> private_cluster
    
    public_cluster - Edge(color="black", style="dotted") - public_rt
    private_cluster - Edge(color="black", style="dotted") - private_rt