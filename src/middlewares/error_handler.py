from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class AgentException(Exception):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        message: str = "Internal Server Error",
        details: str | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(self.message)


async def agent_exception_handler(request: Request, exc: AgentException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.message,
            "details": exc.details,
            "path": request.url.path,
        },
    )


# Common exceptions for reuse
class BadRequestError(AgentException):
    def __init__(self, message: str, details: str | None = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=message,
            details=details,
        )


class NotFoundError(AgentException):
    def __init__(self, message: str, details: str | None = None):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
            details=details,
        )


class UnauthorizedError(AgentException):
    def __init__(self, message: str = "Unauthorized", details: str | None = None):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message=message,
            details=details,
        )


def register_exception_handlers(app: FastAPI) -> None:
    """Register all exception handlers for the application."""
    handlers = {
        AgentException: agent_exception_handler,
        # Add more exception-handler pairs here as needed
    }

    for exception_class, handler in handlers.items():
        app.add_exception_handler(exception_class, handler)
