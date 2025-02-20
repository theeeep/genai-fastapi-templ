from enum import Enum

from pydantic import BaseModel, Field


class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class ChatRequest(BaseModel):
    provider: Provider = Field(..., description="The provider to use for the chat")
    prompt: str = Field(..., description="The input prompt to the model")
    model: str = Field(..., description="The model to use for the chat")
