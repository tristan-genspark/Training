

provider "kubernetes" {
    host = data.aws_eks_cluster.cluster.endpoint
    token = data.aws_eks_cluster_auth.cluster.token
     cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
}

module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "17.1.0"
    cluster_name = "${var.cluster_name}"
    cluster_version = "1.20"
    cluster_create_timeout = "30m" # required to increase since the default value is too short
    subnets = module.vpc.public_subnets
    vpc_id = module.vpc.vpc_id

    node_groups_defaults = {
      ami_type  = "AL2_x86_64"
      disk_size = 10
    }

  node_groups = {
    ram = {
      desired_capacity = 2
      max_capacity     = 10
      min_capacity     = 1
      public_ip = true
      instance_types = ["${var.cluster_node_size}"]
    }
  }
}

data "aws_eks_cluster" "cluster" {
    name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
    name = module.eks.cluster_id
}
