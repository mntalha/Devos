# Commands list that I am following

# activate environment 
conda activate kubernete_env

# go to the Minikube 
cd "C:\Program Files\Kubernetes\Minikube\" 

# start minikube
minikube.exe start

# go to the python MongoDb 
cd "C:\Users\talha\Desktop\MongoDb"

# dockerize
docker build -f Dockerfile -t mongoDB_python:latest .

# tag the python-docker 
docker tag python-client:latest mntalha/mongoDB_python:latest

# send to the docker
docker push mntalha/mongoDB_python:latest

# Kubernetes deployment 
kubectl apply -f deployment.yaml

# check it on the dashboard
minikube dashboard