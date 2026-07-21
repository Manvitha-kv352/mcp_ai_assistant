from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    service = ChatService()

    response = await service.generate_response(
        request.message,
        request.session_id
    )

    return ChatResponse(
        response=response,
        session_id=request.session_id
    )