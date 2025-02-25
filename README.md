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
- Docker and Docker Compose Support

## Project Structure
```
app/
├── core/           # Core functionality and configs
├── database/       # Database models and configuration
├── llm/            # LLM integration
├── middlewares/    # Error handling & middleware
├── modules/        # Feature modules
└── utils/          # Utility functions
```

## Quick Start

### Installation

#### Local Development
```bash
# Clone the repository
git clone <your-repo-url>

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env

# Create initial migration
alembic revision --autogenerate -m "initial_migration"

# Run migrations
alembic upgrade head

# Rollback last migration (if needed)
alembic downgrade -1
```

#### Using Docker
```bash
# Clone the repository
git clone https://github.com/theeeep/genai-fastapi-templ

# Set up environment variables
cp .env.example .env

# Build and start the application with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

### Docker Environment Configuration
The application is configured to run in a Docker environment with PostgreSQL. Make sure your `.env` file contains:

```
# Database Configuration
DB_HOST=db
DB_NAME=genai_template
DB_USER=postgres
DB_PASSWORD=postgres
DB_PORT=5432

# PostgreSQL Container Variables
POSTGRES_DB=genai_template
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Database URL for SQLAlchemy
DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

### Database Configuration
When using SQLAlchemy with asyncpg in Docker, you might need to modify your database connection code to handle SSL settings:

```python
async_engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True,
        future=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=60,
        pool_pre_ping=True,
        connect_args={"ssl": False}  # Disable SSL for local development
    )
)
```

## Running the Application

### Local Development
```bash
# Development
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Docker
```bash
# Start all services
docker-compose up

# Stop all services
docker-compose down

# Rebuild and start
docker-compose up --build
```

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Health Check
```bash
curl http://localhost:8000/health
```

## Troubleshooting
- **Database Connection Issues**: Ensure the database service is running and properly configured in your docker-compose.yml file.
- **Network Issues**: Make sure your services are on the same Docker network as defined in docker-compose.yml.
- **Port Conflicts**: Check if the exposed ports are already in use on your host machine.