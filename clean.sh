# clean up
kubectl delete --all deployments --namespace=authentication
kubectl delete --all services --namespace=authentication
kubectl delete --all pods --namespace=authentication
kubectl delete namespace authentication