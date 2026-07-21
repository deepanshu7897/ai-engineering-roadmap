from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str
    session_id: str