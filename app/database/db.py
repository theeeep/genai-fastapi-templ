import asyncio
import os

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config.settings import Config
from app.core.logger import logger

# Debug prints
logger.info(f"Environment DATABASE_URL: {os.getenv('DATABASE_URL')}")
logger.info(f"Config DATABASE_URL: {Config.DATABASE_URL}")

logger.info(f"Database URL 1: {Config.DATABASE_URL}")

async_engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True,
        future=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=60,
        pool_pre_ping=True,  # Add connection testing
        connect_args={"ssl": False},
    )
)


async def test_connection():
    """Test database connection"""
    try:
        async with async_engine.begin() as conn:
            await conn.execute(text("SELECT 1"))  # Use text() for raw SQL
            logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise


async def init_db():
    """Init db"""
    await test_connection()  # Test connection before initializing
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def close_db():
    """
    Close database connections
    """
    await async_engine.dispose()


async def get_session() -> AsyncSession:
    """
    Get session
    """
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with Session() as session:
        yield session
