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
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(general_router)
app.include_router(chat_router)
app.include_router(upload_router)