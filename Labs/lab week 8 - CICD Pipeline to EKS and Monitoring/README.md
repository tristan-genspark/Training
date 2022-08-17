
###  Tristan S   
## DevOps Lifecycle with AWS: 3 Days

In this project, you’ll be creating the infra using terraform and will perform
application/tool stack configuration using shell scripts and will effectively
use Jenkins for running automated CICD for both the application and infra deployment.

Provisioning a managed EKS cluster and setting up a mutable
environment setup which ensures the HA and Resilience of the application.

Post-Mortem SRE Scoped Project:
Install and configure the monitoring tool stack (Splunk and Dynatrace) to monitor
the Application and Infra which is very essential for every production software system.


### A Break down of the objectives

 -> Creating the infra using terraform  [ managed EKS cluster ]
 -> Use Jenkins for running automated CICD for the application
 -> Set up Dynatrace and Splunk to monitor the application
 -> Make it all highly portable



### Steps Check list and Completion

  ~ = Partial Completion

  [✔️] Setup Jenkins
  
  [✔️] Setup Splunk
 
  [✔️] Create Terraform Script to create an EKS Cluster
  
  [✔️] Make a Working App Deployment on Cluster where its service is accessible
  
  [~] Create a Pipeline in Jenkins  <= (Pipeline was created but there were small issues with permissions)
  
  [✔️] Monitor with Dynatrace  
  
  [x] Monitor with Splunk           <= (We never went over it and I ran out of time)
  
  [✔️] Make Terraform scripts portable and flexible
  
  [✔️] Make the Pipelines portable and flexible

 _________________________________________________

# Step 1 - Setting up an Ec2 for Jenkins and Splunk

Create an Ec2 for the CICD and splunk monitoring

Add the inbound rules TCP 8080 and TCP 8000 for the EC2 security group

For this lab I chose a medium EC2 with 16 Gigabytes of storage

_________________________________________________

# Step 2 - Set up Jenkins on the EC2

```
$ sudo wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo
$ sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
$ sudo amazon-linux-extras install epel -y
$ sudo yum install jenkins -y
$ sudo yum install java-1.8.0 -y
$ sudo systemctl enable jenkins
$ sudo systemctl start jenkins
```

To view the password needed to login
```
$ sudo nano  /var/lib/jenkins/secrets/initialAdminPassword
```

Now visit port 8080 on the public IP to access the Jenkins panel

_________________________________________________

# Step 3 - Set up Splunk on the EC2

```
$ wget -O splunk-9.0.0.1-9e907cedecb1-Linux-x86_64.tgz "https://download.splunk.com/products/splunk/releases/9.0.0.1/linux/splunk-9.0.0.1-9e907cedecb1-Linux-x86_64.tgz"
$ sudo mv splunk-9.0.0.1-9e907cedecb1-Linux-x86_64.tgz /opt
$ cd /opt
$ sudo tar -xvzf splunk-9.0.0.1-9e907cedecb1-Linux-x86_64.tgz
$ sudo /opt/splunk/bin/splunk start
```

I configured splunk to not warn about the minimum disk space for this lab

```
$ sudo vi /opt/splunk/etc/system/local/server.conf
```
edit this file by adding these lines to the end
```
[diskUsage]
minFreeSpace = 50
```

Then I restarted the service

```
$ sudo /opt/splunk/bin/splunk restart
```
Now visit port 8000 on the public IP to access the Splunk panel

_________________________________________________

#      Step 4 - Installing Additional Dependencies And Configuration

Install git
```
$ sudo yum install git -y
```

Install docker
```
$ sudo yum install docker -y
$ sudo systemctl enable docker.service
$ sudo systemctl start docker.service
```

Install Kubectl
```
$ curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.7/2022-06-29/bin/linux/amd64/kubectl
$ chmod +x ./kubectl
$ mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
$ echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
$ kubectl version --short --client
```

Install terraform
```
$ sudo wget https://releases.hashicorp.com/terraform/1.2.7/terraform_1.2.7_linux_amd64.zip
$ sudo unzip terraform_1.2.7_linux_amd64.zip
$ sudo mv terraform /usr/local/bin/
$ terraform version
```

Authenticating Kubectl
```
$ aws configure
$ aws eks --region us-east-1 update-kubeconfig --name EKS-Cluster
```

**Note:** I have learned its important to use the same IAM user used for terraform that is used for the authentication
      of kubectl or it will result in an access denied message. This is something I did that was improved from my
      previous labs.
      
_________________________________________________

# Step 5 - Setting up the Infastructure through terraform

To create the Infastrucutre using Terraform I created multiple terraform files that will create
the virtual private cloud then the subnet within it and create an EKS cluster within it.

Once created, it had a node group within the cluster and a test was done to verify it worked.

```
$ aws configure
$ aws eks --region us-east-2 update-kubeconfig --name EKS-Cluster
$ kubectl get nodes
```

Once it worked I created a node running a test image to confirm the cluster was created correctly.
I was able to connect from the internet to the service on the cluster.

_________________________________________________

# Step 6 - Setting up the Application Deployment Jenkins Pipeline

The pipeline will be an easy step by step creation of the pod and exposing it to the cluster
For this lab I used nginx because of its natrual logs that will be useful for monitoring

Here are the commands that will be executed within the pipeline to deploy the nginx application
The pipeline will have a more refined version of this for the deployment

```
kubectl create deployment nginx-deployment --image=nginx --port=80 --dry-run=client -o yaml > nginx-deploy.yaml
kubectl apply -f nginx-deploy.yaml
```
 
```
kubectl expose deployment nginx-deployment  --type=ClusterIP  --name=nginx-service-cluster-ip
kubectl expose deployment nginx-deployment  --type=NodePort  --name=nginx-service-nodeport
kubectl expose deployment nginx-deployment  --type=LoadBalancer  --name=nginx-service-loadbalancer
```
 

_________________________________________________

# Step 7 - Setting up the Monitoring Tool Stack


For connecting the EKS cluster to Dynatrace this is what I did

Open up the cloud shell Connect to the EKS created

```
aws eks --region us-east-2 update-kubeconfig --name EKS-Cluster
```

Create an agent on Dynatrace and create it as an openshift Agent
once creating the agent make sure to select Kubernetes instead of openshift
Download the dynakube.yaml file

Within the cloud shell go to Actions > Upload File
and upload the dynakube.yaml file

Then copy and paste the commands it says to from the agent page on Dynatrace

Also its possible to connect the AWS cloud to Dynatrace for a wider view
I did this as well


For Connecting Splunk to the webserver

I recall being told we would learn this but we never did and moved on to doing this lab instead.
I tried to find out the best way to do this and I believe that its with universal forwarders but
with the missing understanding of this I spent more time on other parts of this lab and if I had time
come back to this since it would take more time to figure out.

_________________________________________________


# + Addiotnal Steps to make this more portable +

Adding portability to the Jenkins Pipeline
I added parameters to the pipeline to make it more flexible and portable.
When creating the pipeline under the General tab in Jenkins I checked the box for "This project is parameterized"
I then added parameters in to the pipeline code at the top to take these values as input.
string(name: 'portNumber', defaultValue: '80', description: 'Enter the port for the service to listen on')

This makes it possible for the Jenkins pipelines to have changing variables per run.

Adding portability to the Terraform scripts
I added variables that could be changed within the main.tf file for portability.
removing the default option also makes it possible to have it prompt for the values.
If changes are required for the node size or other things within the cluster or VPC it can be set within
the variables in main.tf

_________________________________________________


# + Issues Experienced through this Lab +

Authentication Issues while connecting to the cluster
While getting the cluster set up I had issues with kubectl authentication.
After spending hours on the issue I discovered that because the cluster was created using an IAM user created for terraform
it only had that user as the user that could authenticate for the cluster. I had to authenticate my kubectl using "aws configure"
to use the same IAM user to have access to the cluster. Once I changed this it immediately worked.

The pod status on the cluster was pending and did not end.
I first began by checking on the pod using this command "kubectl describe pod nginx-deployment"
This was because of lack of nodes to run the pod on. I resolved by adding missing nodes to my cluster in terraform.
I discovered that originally my terraform code was broken during the testing so I went back and configured my terraform scripts
and created the cluster again with the new code. After that I made sure the size was correct so there would be no issues with resources
and it worked fine.


