@echo OFF
SET PATH=%PATH%;C:\Program Files (x86)\Terraform
cd terraform-files
terraform init
terraform plan -out=infastructure-plan-release-1
pause
