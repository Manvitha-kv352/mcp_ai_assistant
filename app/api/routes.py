from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to MCP Assistant!"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/config")
def config():
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "model": settings.model_name
    }
    