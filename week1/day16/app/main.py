from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.middleware.request_logger import RequestLoggerMiddleware
from app.middleware.rate_limiter import limiter

from app.routers.auth import router as auth_router
from app.routers.files import router as file_router
from app.routers.ai import router as ai_router

app = FastAPI(
    title="Authentication API",
    version="1.0.0",
)

# -----------------------------
# Rate Limiter
# -----------------------------

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)

app.add_middleware(
    SlowAPIMiddleware,
)

# -----------------------------
# Request Logger
# -----------------------------

app.add_middleware(
    RequestLoggerMiddleware,
)

# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------

app.include_router(auth_router)
app.include_router(file_router)
app.include_router(ai_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI Authentication API"
    }