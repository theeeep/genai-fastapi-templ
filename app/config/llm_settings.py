from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

LLMProvider = Literal["openai", "anthropic"]


class LLMProviderSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    temperature: float = 0.7
    max_tokens: int | None = None
    max_retries: int = 3


class OpenAISettings(LLMProviderSettings):
    api_key: str = Field(alias="OPENAI_API_KEY")
    default_model: str = "gpt-4o"


class AnthropicSettings(LLMProviderSettings):
    api_key: str = Field(alias="ANTHROPIC_API_KEY")
    default_model: str = "claude-3-opus-20240229"
    max_tokens: int | None = 1024


class LLMSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")  # Changed to ignore extra fields

    openai: OpenAISettings = OpenAISettings()
    anthropic: AnthropicSettings = AnthropicSettings()


@lru_cache
def get_llm_settings() -> LLMSettings:
    return LLMSettings()
