from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.schemas.response import Response
from app.database.db import get_session

health_router = APIRouter()


@health_router.get("/health", response_model=Response[dict])
async def health_check(
    session: AsyncSession = Depends(get_session),
):
    try:
        # Test database connection
        await session.exec(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    health_data = {"database": db_status, "api": "healthy"}

    return Response(data=health_data, message="Health check completed")
