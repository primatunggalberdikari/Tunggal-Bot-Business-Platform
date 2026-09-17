"""
Model untuk Log Percakapan.
"""

from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import BaseModel


class ChatLog(BaseModel):
    """Model untuk menyimpan log percakapan bot."""
    __tablename__ = "chat_logs"

    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    user_id = Column(String(50), nullable=False)
    username = Column(String(50), nullable=True)
    message_text = Column(Text, nullable=True)
    response_text = Column(Text, nullable=True)
    intent = Column(String(50), nullable=True)

    tenant = relationship("Tenant", backref="chat_logs")

    def __repr__(self) -> str:
        return f"<ChatLog(id={self.id}, user_id={self.user_id})>"