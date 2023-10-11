# DAT515_TLTYHA
## Docker
Runnin the docker containers should be as easy as:
```bash
docker compose up -d
```

## Kubernetes
For full functionality of the horizontal pod autoscaler, our kubernetes needs a metric server. The easies way to implement this, is using minikube. The minikube metric server can be installed with the following:
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start

minikube addons enable metrics-server
```

Then the docker image needs to be pushed to the minikube cluster:
```bash
docker build -t basic_appv2 . --network=host

minikube image load basic_appv2
```

Now kubernetes is ready for deployment:
```bash
kubectl apply -f .
```
To get the url of the app pod, run the command:
```bash
minikube service app-deploy --url
```
The pod is now accessible localy to the running machine

The HPA should now function. (Note: it might take some time before the first mesurement is made.) Check the recource usage and hpa status using:
```bash
kubectl get hpa
```
