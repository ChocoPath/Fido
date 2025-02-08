# ArgoCD Query Service

## Overview
A FastAPI-based service that provides endpoints to query ArgoCD application statuses and manage deployments.

## Features
- Query ArgoCD application sync status
- List ArgoCD projects and namespaces


## Configuration
Set the following environment variables:
- `ARGOCD_URL`: ArgoCD server URL
- `ARGOCD_TOKEN`: Authentication token

## API Endpoints

### Get Application Status
```http
GET /arogocd/application_status
Authorization: Bearer <token>
```

Response:
```json
{
    "applications": [
        {
            "application_name": "my-app",
            "status": "Synced"
        }
    ]
}
```
<img width="1425" alt="Screenshot 2025-02-07 at 1 54 02 PM" src="https://github.com/user-attachments/assets/05656c8d-5a36-4ebf-9249-bce916c330d7" />




### List Projects
```http
GET /arogocd/list_projects
Authorization: Bearer <token>
```

Response:
```json
{
    "projects": [
        {
            "project_name": "default",
            "description": "Default project"
        },
    ]
}
```
<img width="1426" alt="Screenshot 2025-02-07 at 1 53 15 PM" src="https://github.com/user-attachments/assets/5e7d8cf0-1b8c-4a3a-b1c2-fda53ad8270d" />




## API Documentation
- Swagger UI: `http://localhost:8000/docs`
