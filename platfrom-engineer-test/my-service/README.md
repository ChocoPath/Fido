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

## API Documentation
- Swagger UI: `http://localhost:8000/docs`