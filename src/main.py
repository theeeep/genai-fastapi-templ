# src/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.logger import logger
from src.database.db import close_db, init_db
from src.middlewares.error_handler import register_exception_handlers
from src.modules.chat.router import chat_router
from src.modules.health.router import health_router

logger.info("Main Application")


@asynccontextmanager
async def life_span(app: FastAPI):
    logger.info("🚀 Starting Application...")
    await init_db()
    logger.info("✅ Application Started Successfully...")
    yield
    logger.info("🛑 Stopping Application...")
    await close_db()  # Add this line
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
app.include_router(health_router, tags=["Health"])  # No version prefix for health endpoint
