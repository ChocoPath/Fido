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
![plot](/images/Screenshot 2025-02-07 at 1.54.02 PM.png)


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

![Alt Text](/images/Screenshot 2025-02-07 at 1.53.15 PM.png)

## API Documentation
- Swagger UI: `http://localhost:8000/docs`