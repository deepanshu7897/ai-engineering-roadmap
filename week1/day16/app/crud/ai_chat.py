from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ai_chat import AIChat


async def save_chat(
    db: AsyncSession,
    session_id: str,
    prompt: str,
    response: str,
):
    chat = AIChat(
        session_id=session_id,
        prompt=prompt,
        response=response,
    )

    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat


async def get_chat_history(
    db: AsyncSession,
    session_id: str,
):
    result = await db.execute(
        select(AIChat)
        .where(AIChat.session_id == session_id)
        .order_by(AIChat.created_at.asc())
    )

    return result.scalars().all()