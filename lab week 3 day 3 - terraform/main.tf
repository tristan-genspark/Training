//
// Tristan S
//
// Project - Terraform Lab Week 3 Day 3
//
// Using Terraform to create a VPC
//
//
// References
// Create VPC: https://github.com/bugbiteme/demo-tform-aws-vpc/blob/master/modules/networking/main.tf
// Create SSH Key: https://github.com/bugbiteme/demo-tform-aws-vpc/blob/master/modules/ssh-key/main.tf
// Create Ec2: https://github.com/bugbiteme/demo-tform-aws-vpc/blob/master/modules/ec2/main.tf
// Example of Terraform by Trainer: https://github.com/devopshubproject/ec2-jenkins-tf
// Setting Route Table: https://stackoverflow.com/questions/51852034/terraform-aws-how-to-add-default-route-to-vpc-default-route-table
//                        

provider "aws" {
region = "us-east-1"
access_key = "put your access key here"
secret_key = "put your secret key here"
}

variable "labname" {
  type = string
  default = "terraform-test"
}

data "aws_availability_zones" "az" {
  state = "available"
}


// =============== ( Create SSH Key )

resource "tls_private_key" "sshkey" {
    algorithm = "RSA"
    rsa_bits = 4096
}

resource "local_file" "private_key" {
    content = tls_private_key.sshkey.private_key_pem
    filename = "key.pem"
    file_permission = "0600"
}
resource "aws_key_pair" "ssh_pvt_key" {
    key_name = "terraform-test-ssh-key"
    public_key = tls_private_key.sshkey.public_key_openssh
}



// =============== ( Create VPC )


resource "aws_vpc" "vpc" {

  cidr_block = "10.0.0.0/16"
  instance_tenancy = "default"
  enable_dns_support = true
  enable_dns_hostnames = true


}

// Create the Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id
}

// Create the Subnet
resource "aws_subnet" "public1" {
  vpc_id = aws_vpc.vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.az.names[0]
  map_public_ip_on_launch = true
}

// Create the route table
resource "aws_route" "route_to_internet" {
  route_table_id         = aws_vpc.vpc.default_route_table_id
  destination_cidr_block = "0.0.0.0/0" //  Intenernet Access
  gateway_id             = aws_internet_gateway.igw.id
}


// =============== ( Add Security Group and Rules )


// Create security group
resource "aws_security_group" "sg" {
  name        = "terraform-created-sg"
  description = "testing and learning"
  vpc_id      =  aws_vpc.vpc.id

  ingress {
  from_port = 22
  to_port = 22
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}




// =============== ( Create the Ec2 Within the newly created VPC )


// Create aws_ami filter to pick up the ami available in your region
data "aws_ami" "amazon-linux-2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

// Configure the EC2 instance in a public subnet
resource "aws_instance" "ec2_public" {
  ami                         = data.aws_ami.amazon-linux-2.id
  associate_public_ip_address = true
  instance_type               = "t2.micro"
  key_name                    = aws_key_pair.ssh_pvt_key.key_name
  subnet_id                   = aws_subnet.public1.id
  vpc_security_group_ids      = [aws_security_group.sg.id]


  connection {
    type     = "ssh"
    user     = "ec2-user"
    password = "ec2-learning-terraform22"
    host     = self.public_ip
  }



  }
