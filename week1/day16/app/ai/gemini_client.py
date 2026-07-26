import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    # -----------------------------
    # Text Generation
    # -----------------------------
    def generate(self, prompt: str) -> str:
        for _ in range(3):
            try:
                response = self.client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt,
                )
                return response.text

            except Exception:
                print("Gemini busy... retrying in 5 seconds...")
                time.sleep(5)

        raise Exception("Gemini API is temporarily unavailable.")

    # -----------------------------
    # Streaming
    # -----------------------------
    async def stream_content(self, prompt: str):
        stream = self.client.models.generate_content_stream(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        for chunk in stream:
            if chunk.text:
                yield chunk.text

    # -----------------------------
    # Single Embedding
    # -----------------------------
    def embed_text(
        self,
        text: str,
        task_type: str = "RETRIEVAL_DOCUMENT",
    ) -> list[float]:

        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
            config=types.EmbedContentConfig(
                task_type=task_type,
            ),
        )

        return response.embeddings[0].values

    # -----------------------------
    # Batch Embeddings
    # -----------------------------
    def embed_batch(
        self,
        texts: list[str],
        task_type: str = "RETRIEVAL_DOCUMENT",
    ) -> list[list[float]]:

        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=texts,
            config=types.EmbedContentConfig(
                task_type=task_type,
            ),
        )

        return [embedding.values for embedding in response.embeddings]