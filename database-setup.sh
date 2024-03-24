kubectl apply -f config/mysql/pv.yaml
kubectl apply -f config/mysql/pvc.yaml
kubectl apply -f config/mysql/deployment.yaml
kubectl apply -f config/mysql/service.yaml