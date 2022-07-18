//
// Tristan S
//
// Lab 3 Friday
//
//


provider "aws" {
region = "us-east-1"
access_key = "Put Access Key Here"
secret_key = "Put Secret Key Here"
}

variable "labname" {
  type = string
  default = "friday-lab-test"
}
