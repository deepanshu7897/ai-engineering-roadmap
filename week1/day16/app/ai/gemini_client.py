import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

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

    async def stream_content(self, prompt: str):
        stream = self.client.models.generate_content_stream(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        for chunk in stream:
            if chunk.text:
                yield chunk.text