
For this lab I took an example Nginx pod and ran it 

cat <<EOF > nginx-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
EOF

kubectl apply -f nginx-deployment.yaml

And exposed it 
kubectl expose deployment nginx-deployment  --type=ClusterIP  --name=nginx-service-cluster-ip
kubectl expose deployment nginx-deployment  --type=NodePort  --name=nginx-service-nodeport
kubectl expose deployment nginx-deployment  --type=LoadBalancer  --name=nginx-service-loadbalancer


I went to the the amazon cloud shell for the region the EKS was located on

I created the file on my computer named tcp-liveness-readiness.yaml
then I uploaded it to the cloud shell using the built in upload feature

Add the code from the "TCP liveness probe" section found here to the file
https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
as seen below

apiVersion: v1
kind: Pod
metadata:
  name: goproxy
  labels:
    app: goproxy
spec:
  containers:
  - name: goproxy
    image: k8s.gcr.io/goproxy:0.1
    ports:
    - containerPort: 8080
    readinessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20

I uploaded the created file to the clouds shell enviornment

I applied the uploaded yaml file to deploy the pod
kubectl apply -f tcp-liveness-readiness.yaml

To view its status I did this command
kubectl describe pod goproxy




