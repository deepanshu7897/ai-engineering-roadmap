from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list(config={"page_size": 100}):
    if hasattr(model, "supported_actions"):
        if "generateContent" in model.supported_actions:
            print(model.name)