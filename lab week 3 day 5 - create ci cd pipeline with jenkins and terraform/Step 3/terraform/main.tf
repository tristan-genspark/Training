//
// Tristan S
//
// Lab 3 Friday
//
//

// Good Reference
// https://medium.com/geekculture/deploy-an-aws-eks-cluster-using-terraform-965fe680f9d4
//


provider "aws" {
region = "us-east-1"
access_key = "AKIA4LSI336NNX3XUW7V"
secret_key = "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"
}

variable "labname" {
  type = string
  default = "friday-lab-test"
}
