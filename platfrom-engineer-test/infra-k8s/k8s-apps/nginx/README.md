# Nginx App Deployment Guide

This guide provides the steps to deploy and run the Nginx app in an ArgoCD pipeline. The app runs on port 8001 using port forwarding.

## Prerequisites

- Kubernetes cluster
- ArgoCD installed and configured
- `kubectl` installed and configured
- `argocd` CLI installed and configured

## Steps

1. **Change directory**

    ```sh
    cd platfrom-engineer-test/infra-k8s/k8s-apps/nginx
    ```

2. **Apply the Kubernetes Manifests**

    ```sh
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

3. **Deploy the App using ArgoCD**

    - Login to ArgoCD:

      ```sh
      argocd login <argocd-server>
      ```

    - Create a new application in ArgoCD:

      ```sh
      kubectl apply -f nginx-argocd-app.yaml
      ```

    - Sync the application:

      ```sh
      argocd app sync nginx-app
      ```

4. **Port Forwarding**

    To access the Nginx app, set up port forwarding:

    ```sh
    kubectl port-forward svc/nginx-service 8001:80
    ```

5. **Access the Nginx App**

    Open your browser and navigate to `http://localhost:8001`.
