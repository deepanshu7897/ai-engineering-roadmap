from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Authentication API"

    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"

    SECRET_KEY: str = "your-secret-key"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()