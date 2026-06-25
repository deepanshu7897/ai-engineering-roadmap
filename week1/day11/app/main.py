from fastapi import FastAPI

from app.routers.documents import router

app = FastAPI(
    title="AI Engineering Roadmap - Day 11"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Day 11"
    }