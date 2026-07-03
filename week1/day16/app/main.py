from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.files import router as file_router

app = FastAPI(
    title="Authentication API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(file_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI Authentication API"
    }