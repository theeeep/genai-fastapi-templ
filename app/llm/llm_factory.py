from langchain.chat_models.base import BaseChatModel
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from app.config.llm_settings import get_llm_settings
from app.middlewares.error_handler import AgentException


class LLMFactory:
    @staticmethod
    def create_llm(provider: str, model_name: str) -> BaseChatModel:
        try:
            settings = get_llm_settings()

            if provider == "openai":
                return ChatOpenAI(
                    api_key=settings.openai.api_key,
                    model_name=model_name,
                    temperature=settings.openai.temperature,
                    max_tokens=settings.openai.max_tokens,
                )
            elif provider == "anthropic":
                return ChatAnthropic(
                    api_key=settings.anthropic.api_key,
                    model=model_name,
                    temperature=settings.anthropic.temperature,
                    max_tokens=settings.anthropic.max_tokens,
                )
            else:
                raise AgentException(status_code=400, message="Invalid Provider", details=f"Provider {provider} is not supported")
        except Exception as e:
            raise AgentException(status_code=500, message="LLM Creation Failed", details=str(e)) from e
