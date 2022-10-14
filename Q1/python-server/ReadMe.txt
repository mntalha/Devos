# Commands list that I am following

# activate environment 
conda activate kubernete_env

# go to the Minikube 
cd "C:\Program Files\Kubernetes\Minikube\" 

# start minikube
minikube.exe start

# go to the python server
cd "C:\Users\talha\Desktop\kubernete\python-server"

# dockerize
docker build -f Dockerfile -t python-server:latest .

# tag the python-docker 
docker tag server-python:latest mntalha/server-python:latest

# send to the docker
docker push mntalha/python-server:latest

# Kubernetes deployment 
kubectl apply -f deployment.yaml

# check it on the dashboard
minikube dashboard