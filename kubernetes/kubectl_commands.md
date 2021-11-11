# Namespace
```
kubectl apply -f 1-namespace.yml
kubectl get ns
```
# Deployment
```
kubectl apply -f 2-deployment.yml
kubectl get deployments -n <<namespace>>
```
# Service
```
kubectl apply -f 3-service.yml
kubectl get service -n <<namespace>>
```
# Ingress
```
kubectl apply -f 4-ingress.yml
kubectl get ingress -n <<namespace>>
```
# Horizontal Pod Autoscaler
```
kubectl apply -f 5-hpa.yml
kubectl get hpa -n <<namespace>>
```