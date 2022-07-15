I have created a jenkins file that fully automates the creation of a docker container
as well as runs a test on it by running a script that verifies the page is accessable.

The docker container contains a small python application that sends a webpage to any browser connecting
from port 80 
 
one the creation of the docker file and the testing of it is complete it will use dockers push command to 
push it on to AWS through ECR.

I had issues with commands within jenkins working properly resulting in it having authentication issues
but I have tested and was able to manually run the push command in docker to push the created and tested
container on to ECR on AWS.
 
 

Stage 1 Building 
   Build the docker container  

   Pack the python script and its dependencies in to a docker container

Stage 2 Testing

   Run the docker container within jenkins

   Run the test script to connect and verify the container is working 

   Stop the container

Stage 3 Deployment
   
    Tag the Docker container for deploymenet

    Push the Docker container to ECR 

    Remove the local image created 






   