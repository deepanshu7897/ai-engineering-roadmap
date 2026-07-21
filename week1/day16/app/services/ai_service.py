from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.gemini_client import GeminiClient
from app.crud.ai_chat import save_chat, get_chat_history

client = GeminiClient()


async def generate_ai_response(
    db: AsyncSession,
    prompt: str,
    session_id: str,
):
    history = await get_chat_history(db, session_id)

    conversation = ""

    for chat in history:
        conversation += f"User: {chat.prompt}\n"
        conversation += f"Assistant: {chat.response}\n\n"

    conversation += f"User: {prompt}\nAssistant:"

    response = client.generate(conversation)

    await save_chat(
        db=db,
        session_id=session_id,
        prompt=prompt,
        response=response,
    )

    return response


async def fetch_chat_history(
    db: AsyncSession,
    session_id: str,
):
    return await get_chat_history(db, session_id)