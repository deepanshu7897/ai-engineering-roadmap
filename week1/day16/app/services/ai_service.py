from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.conversation_manager import ConversationManager
from app.ai.gemini_client import GeminiClient
from app.ai.guardrails import Guardrails
from app.ai.response_metrics import ResponseMetrics
from app.crud.ai_chat import get_chat_history, save_chat
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import Retriever
from app.schemas.ai_response import AIResponse

client = GeminiClient()

conversation_manager = ConversationManager(
    max_messages=10,
)

guardrails = Guardrails()

metrics = ResponseMetrics()

retriever = Retriever()


async def generate_ai_response(
    db: AsyncSession,
    prompt: str,
    session_id: str,
) -> AIResponse:

    # -----------------------------
    # Validate Input
    # -----------------------------
    guardrails.check(prompt)

    # -----------------------------
    # Retrieve Context
    # -----------------------------
    context = retriever.retrieve(
        query=prompt,
        top_k=3,
    )

    # -----------------------------
    # Conversation History
    # -----------------------------
    history = await get_chat_history(
        db=db,
        session_id=session_id,
    )

    conversation = conversation_manager.build_conversation(
        history=history,
        current_prompt=prompt,
    )

    # -----------------------------
    # Build RAG Prompt
    # -----------------------------
    rag_prompt = PromptBuilder.build(
        question=prompt,
        context=context,
        conversation=conversation,
    )

    # -----------------------------
    # Generate Response
    # -----------------------------
    metrics.start()

    response = client.generate(rag_prompt)

    response_time = metrics.stop()

    # -----------------------------
    # Save Chat
    # -----------------------------
    await save_chat(
        db=db,
        session_id=session_id,
        prompt=prompt,
        response=response,
    )

    # -----------------------------
    # Metrics
    # -----------------------------
    total_text = rag_prompt + response

    tokens = metrics.estimate_tokens(total_text)

    cost = metrics.estimate_cost(tokens)

    return AIResponse(
        success=True,
        response=response,
        session_id=session_id,
        response_time=response_time,
        tokens_used=tokens,
        estimated_cost=cost,
    )


async def fetch_chat_history(
    db: AsyncSession,
    session_id: str,
):
    return await get_chat_history(
        db=db,
        session_id=session_id,
    )