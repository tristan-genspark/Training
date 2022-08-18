//
// Tristan S
//
// This Terraform Script is used to create a VPC containing a subnet that has an EKS with cluster nodes
//
//  VPC
//    ^--- Subnet
//             ^----- EKS Cluster
//                            ^------ Cluster Nodes
//



// Remove the default="" values for prompting in the terminal


variable "region" {
  type = string
  description = "The region the VPC will be placed within."
  default = "us-west-1"
}

variable "vpc_name" {
  type        = string
  description = "The name assigned to the VPC that will be created."
  default = "Training-Lab-VPC"
}

variable "cluster_name" {
  type        = string
  description = "The name assigned to the EKS Cluster that will be created."
  default = "EKS-Cluster"
}

variable "cluster_node_size" {
  type        = string
  description = "The instance size created for the cluster nodes. (Examples: t2.micro ,t2.small, t2.medium, c5.large)"
  default = "t2.small"
}
