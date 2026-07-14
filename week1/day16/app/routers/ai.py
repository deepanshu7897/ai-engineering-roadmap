from fastapi import APIRouter

from app.ai.gemini_client import GeminiClient
from app.schemas.ai import PromptRequest

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)

client = GeminiClient()


@router.post("/generate")
def generate_text(request: PromptRequest):
    response = client.generate(request.prompt)

    return {
        "response": response
    }