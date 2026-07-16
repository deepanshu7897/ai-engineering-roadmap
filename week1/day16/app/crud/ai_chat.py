from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ai_chat import AIChat


async def save_chat(
    db: AsyncSession,
    prompt: str,
    response: str,
):
    from sqlalchemy import select


async def get_chat_history(db: AsyncSession):
    result = await db.execute(
        select(AIChat).order_by(AIChat.created_at.desc())
    )

    return result.scalars().all()
    chat = AIChat(
        prompt=prompt,
        response=response,
    )

    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat