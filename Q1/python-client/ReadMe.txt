# Commands list that I am following

# activate environment 
conda activate kubernete_env

# go to the Minikube 
cd "C:\Program Files\Kubernetes\Minikube\" 

# start minikube
minikube.exe start

# go to the python client 
cd "C:\Users\talha\Desktop\kubernete\python-client"

# dockerize
docker build -f Dockerfile -t python-client:latest .

# tag the python-docker 
docker tag python-client:latest mntalha/python-client:latest

# send to the docker
docker push mntalha/python-client:latest

# Kubernetes deployment 
kubectl apply -f deployment.yaml

# check it on the dashboard
minikube dashboard