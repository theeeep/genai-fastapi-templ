from fastapi import APIRouter

from .schema import ChatRequest, ChatResponse
from .service import ChatService

chat_router = APIRouter()


@chat_router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await ChatService.process_chat_request(request)
