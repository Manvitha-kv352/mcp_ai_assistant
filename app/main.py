from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as general_router
from app.api.chat import router as chat_router
from app.core.settings import settings
from app.api.upload import router as upload_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="An MCP-powered AI Assistant."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(general_router)
app.include_router(chat_router)
app.include_router(upload_router)