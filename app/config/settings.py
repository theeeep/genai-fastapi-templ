from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class
    """

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/genai_template"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        ase_sensitive=True,
    )


Config = Settings()
