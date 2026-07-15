from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.gemini_client import GeminiClient
from app.crud.ai_chat import save_chat

client = GeminiClient()


async def generate_ai_response(
    db: AsyncSession,
    prompt: str,
):
    response = client.generate(prompt)

    await save_chat(
        db=db,
        prompt=prompt,
        response=response,
    )

    return response