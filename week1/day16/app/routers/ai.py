from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.gemini_client import GeminiClient
from app.db.database import get_db
from app.schemas.ai import PromptRequest
from app.services.ai_service import (
    generate_ai_response,
    fetch_chat_history,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)

gemini = GeminiClient()


@router.post("/generate")
async def generate_text(
    request: PromptRequest,
    db: AsyncSession = Depends(get_db),
):
    response = await generate_ai_response(
        db=db,
        prompt=request.prompt,
        session_id=request.session_id,
    )

    return {
        "response": response
    }


@router.get("/history/{session_id}")
async def get_history(
    session_id: str,
    db: AsyncSession = Depends(get_db),
):
    history = await fetch_chat_history(
        db=db,
        session_id=session_id,
    )

    return history


@router.post("/stream")
async def stream_ai_response(request: PromptRequest):

    async def event_generator():
        async for chunk in gemini.stream_content(request.prompt):
            yield f"data: {chunk}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )