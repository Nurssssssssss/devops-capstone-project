# Kubernetes deployment

Build the image and make it available to your cluster before applying these
manifests. Create the database Secret separately; do not commit credentials:

```sh
kubectl create secret generic accounts-db \
  --from-literal=database-uri='postgresql://USER:PASSWORD@HOST:5432/DB'
kubectl apply -f deployment.yaml
kubectl rollout status deployment/accounts
kubectl get deployment,pods,replicasets,service
kubectl port-forward service/accounts 8080:8080
```

Then open http://localhost:8080/ in the cluster's forwarded browser or run
`curl http://localhost:8080/`. For Minikube, load the local image with
`minikube image load accounts:latest`.
