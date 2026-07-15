from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class AIChat(Base):
    __tablename__ = "ai_chats"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())