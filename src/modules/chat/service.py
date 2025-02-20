from langchain_core.messages import HumanMessage

from src.llm.llm_factory import LLMFactory

from .schema import ChatRequest


class ChatService:
    @staticmethod
    async def process_chat_request(request: ChatRequest) -> str:
        """Process the chat request"""
        llm = LLMFactory.create_llm(request.provider, request.model)
        message = [HumanMessage(content=request.prompt)]
        response = llm.invoke(message)
        return response.content
