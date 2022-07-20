

provider "kubernetes" {
    host = data.aws_eks_cluster.cluster.endpoint
    token = data.aws_eks_cluster_auth.cluster.token
     cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
}

module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "17.1.0"
    cluster_name = local.cluster_name
    cluster_version = "1.20"
    //subnets = module.vpc.private_subnets
    subnets = module.vpc.public_subnets

    tags = {
        Name = "Friday-Lab-EKS-Cluster"
    }

    vpc_id = module.vpc.vpc_id
    workers_group_defaults = {
        root_volume_type = "gp2"
    }

    worker_groups = [
        {
            name = "Node-1"
            instance_type = "t2.micro"
            asg_desired_capacity = 2
            additional_security_group_ids = [aws_security_group.worker_group_mgmt_one.id]
        },
        {
            name = "Node-2"
            instance_type = "t2.micro"
            asg_desired_capacity = 1
            additional_security_group_ids = [aws_security_group.worker_group_mgmt_two.id]
        },
    ]
}

data "aws_eks_cluster" "cluster" {
    name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
    name = module.eks.cluster_id
}
