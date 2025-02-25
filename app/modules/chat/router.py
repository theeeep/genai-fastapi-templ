from uuid import uuid4

from fastapi import APIRouter, status

from app.core.schemas.response import Response
from app.middlewares.error_handler import AgentException, BadRequestError

from .schema import ChatRequest
from .service import ChatService

chat_router = APIRouter()


@chat_router.post("/chat", response_model=Response[str])
async def chat(request: ChatRequest) -> Response[str]:
    request_id = str(uuid4())
    try:
        result = await ChatService.process_chat_request(request)
        return Response(
            status=status.HTTP_200_OK,
            message="Chat response generated successfully",
            data=result,
            request_id=request_id,
        )
    except Exception as e:
        if "you must provide a model parameter" in str(e):
            raise BadRequestError(message="Invalid model configuration", details="Model parameter is required for the selected provider")
        raise AgentException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Chat service error", details=str(e)) from e
