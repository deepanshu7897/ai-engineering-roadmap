from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

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


@router.post("/generate")
@router.get("/history")
async def get_history(
    db: AsyncSession = Depends(get_db),
):
    history = await fetch_chat_history(db)

    return history
async def generate_text(
    request: PromptRequest,
    db: AsyncSession = Depends(get_db),
):
    response = await generate_ai_response(
        db=db,
        prompt=request.prompt,
    )

    return {
        "response": response
    }