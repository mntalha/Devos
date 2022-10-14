

conda activate kubernete_env

cd "C:\Program Files\Kubernetes\Minikube\" 

minikube.exe start

cd "C:\Users\talha\Desktop\Helm"

docker build -f Dockerfile -t fastapi_python:latest .

docker tag fastapi_python:latest mntalha/fastapi_python:latest

docker push mntalha/fastapi_python:latest

helm create fast_api

in values,,,

image:
  repository: mntalha/fastapi-python
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: 0.1.0


 image: mntalha/fastapi-python
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 8000

 ../helm install talha.\fastapi\


NAME: fastapi
LAST DEPLOYED: Thu Oct 13 23:34:01 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=fastapi,app.kubernetes.io/instance=fastapi" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
(kubernete_env) PS C:\Users\talha\Desktop\windows-amd64\Helm>

minikube service talha-fastapi