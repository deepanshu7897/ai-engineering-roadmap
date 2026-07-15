from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ai_chat import AIChat


async def save_chat(
    db: AsyncSession,
    prompt: str,
    response: str,
):
    chat = AIChat(
        prompt=prompt,
        response=response,
    )

    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat