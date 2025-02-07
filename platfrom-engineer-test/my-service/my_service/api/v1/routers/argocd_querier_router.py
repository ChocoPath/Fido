
from fastapi import FastAPI, Depends
from my_service.dependencies import get_token
from my_service.utils.logger import setup_logger
from fastapi import APIRouter
from fastapi import HTTPException
from my_service.config.config import settings
import httpx


router = APIRouter(
    prefix="/arogocd",
    tags=["arogocd"],
)


logger = setup_logger()


app = FastAPI()



@router.get("/application_status")
async def application_status(token: str = Depends(get_token)):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient(verify=False) as client:
        try:
            # Call ArgoCD API to list applications
            response = await client.get(f"https://{settings.ARGOCD_URL}/api/v1/applications", headers=headers)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Error fetching application status: {str(e)}")

    # Process response data
    applications_data = response.json().get("items", [])
    applications_status = [
        {
            "application_name": app.get("metadata", {}).get("name", "unknown"),
            "status": app.get("status", {}).get("sync", {}).get("status", "Unknown")
        }
        for app in applications_data
    ]

    # Return the formatted response
    return {"applications": applications_status}


@router.get("/list_projects")
async def list_projects(token: str = Depends(get_token)):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient(verify=False) as client:
        try:
            # Call ArgoCD API to get list of projects
            response = await client.get(f"https://{settings.ARGOCD_URL}/api/v1/projects", headers=headers)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Error fetching projects: {str(e)}")

    # Process response data
    projects_data = response.json().get("items", [])
    projects_list = [
        {
            "project_name": project.get("metadata", {}).get("name", "unknown"),
            "namespace": project.get("metadata", {}).get("namespace", "argocd")
        }
        for project in projects_data
    ]

    return {"projects": projects_list}
