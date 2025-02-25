# Gen AI Application Template

A production-ready FastAPI template for building AI applications with LangChain integration.

## Features
- Multiple LLM Provider Support (OpenAI, Anthropic)
- Standardized Response Handling
- Global Error Management
- Modular Project Structure
- Type Safety with Pydantic
- Async Support
- Logging System
- Database Integration with SQLModel
- Migration Support with Alembic

## Project Structure
src/
├── core/           # Core functionality and configs
├── database/       # Database models and configuration
├── llm/            # LLM integration
├── middlewares/    # Error handling & middleware
├── modules/        # Feature modules
└── utils/          # Utility functions



## Quick Start

### Installation
```bash
# Clone the repository
git clone <your-repo-url>

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Create initial migration
alembic revision --autogenerate -m "initial_migration"

# Run migrations
alembic upgrade head

# Rollback last migration (if needed)
alembic downgrade -1

Running the Application

# Development
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000

API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Health Check
curl http://localhost:8000/health