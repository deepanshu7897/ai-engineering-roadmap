from pydantic import BaseModel, Field


class AIResponse(BaseModel):
    success: bool
    response: str
    session_id: str
    response_time: float
    tokens_used: int
    estimated_cost: float

    sources: list[dict] = Field(default_factory=list)