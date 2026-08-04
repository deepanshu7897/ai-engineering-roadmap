class PromptBuilder:
    @staticmethod
    def build(
        question: str,
        context: str,
        conversation: str,
    ) -> str:

        return f"""
You are a helpful AI assistant.

You must answer ONLY using the retrieved document context.

Rules:
1. Answer from the retrieved context whenever possible.
2. Use conversation history only if it helps clarify the user's question.
3. If the answer is not found in the retrieved context, reply exactly:
   "I couldn't find that information in the uploaded document."
4. Do not hallucinate.
5. Do not invent facts.

========================
Retrieved Context
========================

{context}

========================
Conversation History
========================

{conversation}

========================
User Question
========================

{question}

Assistant:
"""