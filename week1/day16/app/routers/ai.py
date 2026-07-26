from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.gemini_client import GeminiClient
from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.ai import PromptRequest
from app.schemas.ai_response import AIResponse
from app.services.ai_service import (
    generate_ai_response,
    fetch_chat_history,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)

gemini = GeminiClient()


@router.post(
    "/generate",
    response_model=AIResponse,
)
async def generate_text(
    request: PromptRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await generate_ai_response(
        db=db,
        prompt=request.prompt,
        session_id=current_user.username,
    )


@router.get("/history")
async def get_history(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    history = await fetch_chat_history(
        db=db,
        session_id=current_user.username,
    )

    return history


@router.post("/stream")
async def stream_ai_response(
    request: PromptRequest,
    current_user: User = Depends(get_current_user),
):
    async def event_generator():
        async for chunk in gemini.stream_content(request.prompt):
            yield f"data: {chunk}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )