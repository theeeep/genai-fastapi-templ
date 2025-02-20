# src/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.logger import logger
from src.middlewares.error_handler import register_exception_handlers
from src.modules.chat.router import chat_router

logger.info("Main Application")


@asynccontextmanager
async def life_span(app: FastAPI):
    logger.info("🚀 Starting Application...")
    logger.info("✅ Application Started Successfully...")
    yield
    logger.info("🛑 Stopping Application...")
    logger.info("👋 Application Stopped Successfully...")


version = "v1"
title = "FastAPI Template"
description = "A fastapi template for developers"

app = FastAPI(
    version=version,
    title=title,
    description=description,
    lifespan=life_span,
)

register_exception_handlers(app)

app.include_router(chat_router, prefix=f"/{version}", tags=["Chat"])
