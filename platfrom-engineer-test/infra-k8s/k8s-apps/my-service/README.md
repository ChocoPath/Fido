# My Service Deployment

This document provides instructions for deploying `my-service` using Argo CD and Kubernetes manifests.

## Prerequisites

- Kubernetes cluster
- Argo CD installed and configured
- `kubectl` configured to interact with your cluster

## Files

- `argocd-app.yaml`: Argo CD application definition
- `deployment.yaml`: Kubernetes Deployment manifest
- `service.yaml`: Kubernetes Service manifest

## Deployment Steps

### 1. Deploy Argo CD Application

Apply the Argo CD application manifest to create an Argo CD application that will manage the deployment of `my-service`.

```sh
kubectl apply -f argocd-app.yaml
```

### 2. Deploy Kubernetes Resources

Apply the Kubernetes manifests to deploy the `my-service` application.

```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 3. Verify Deployment

Check the status of the deployment and service to ensure they are running correctly.

```sh
kubectl get deployments
kubectl get services
```

<img width="1680" alt="Screenshot 2025-02-08 at 10 38 27 AM" src="https://github.com/user-attachments/assets/a171cd0d-e785-47f3-9cd9-899864ced286" />


## Cleanup

To remove the deployed resources, delete the Argo CD application and Kubernetes resources.

```sh
kubectl delete -f argocd-app.yaml
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```
