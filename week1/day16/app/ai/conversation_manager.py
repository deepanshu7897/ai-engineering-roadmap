from app.models.ai_chat import AIChat


class ConversationManager:
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages

    def build_conversation(
        self,
        history: list[AIChat],
        current_prompt: str,
    ) -> str:

        history = history[-self.max_messages:]

        conversation = []

        system_prompt = (
            "You are a helpful AI assistant. "
            "Answer clearly and accurately. "
            "Use previous conversation whenever it is relevant."
        )

        conversation.append(system_prompt)
        conversation.append("")

        for chat in history:
            conversation.append(f"User: {chat.prompt}")
            conversation.append(f"Assistant: {chat.response}")
            conversation.append("")

        conversation.append(f"User: {current_prompt}")
        conversation.append("Assistant:")

        return "\n".join(conversation)