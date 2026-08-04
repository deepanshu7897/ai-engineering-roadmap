import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class EmbeddingService:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-embedding-001"

    def embed_text(self, text: str) -> list[float]:
        response = self.client.models.embed_content(
            model=self.model,
            contents=text,
        )

        return response.embeddings[0].values

    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return [
            self.embed_text(text)
            for text in texts
        ]