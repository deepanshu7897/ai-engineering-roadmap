from app.ai.gemini_client import GeminiClient

client = GeminiClient()

response = client.generate(
    "Explain FastAPI in exactly two sentences."
)

print(response)