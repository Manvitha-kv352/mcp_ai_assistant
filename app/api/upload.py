import logging
import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.indexing_service import IndexingService
from app.session.session_manager import SessionManager

logger = logging.getLogger(__name__)
router = APIRouter()
indexing_service = IndexingService()
session_manager = SessionManager()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    session_id: str = Form(default="")
):

    target_session_id = session_id or "default-session"

    session_manager.create_session(target_session_id)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    count = indexing_service.index_pdf(file_path)

    session_manager.add_document(target_session_id, file.filename)

    return {
        "message": "PDF uploaded and indexed successfully",
        "filename": file.filename,
        "chunks_indexed": count,
        "session_id": target_session_id,
    }