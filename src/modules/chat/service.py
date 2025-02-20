from langchain_core.messages import HumanMessage

from src.llm.llm_factory import LLMFactory
from src.middlewares.error_handler import AgentException

from .schema import ChatRequest, ChatResponse


class ChatService:
    @staticmethod
    async def process_chat_request(request: ChatRequest) -> ChatResponse:
        try:
            llm = LLMFactory.create_llm(request.provider, request.model)

            message = [HumanMessage(content=request.prompt)]

            response = llm.invoke(message)

            return ChatResponse(response=response.content)

        except Exception as e:
            raise AgentException(
                status_code=500,
                message="Failed to create LLM",
                details=str(e),
            ) from e
