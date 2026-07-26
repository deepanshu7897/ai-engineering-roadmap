from pydantic import BaseModel


class AIResponse(BaseModel):
    success: bool
    response: str
    session_id: str
    response_time: float
    tokens_used: int
    estimated_cost: float