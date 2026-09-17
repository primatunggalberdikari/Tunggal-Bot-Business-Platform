"""
Model untuk Tenant (UMKM).
Setiap UMKM adalah satu tenant dengan chat_id unik.
"""

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
from .base import BaseModel


class Tenant(BaseModel):
    """Model untuk menyimpan data UMKM."""
    __tablename__ = "tenants"
    
    name = Column(String(100), nullable=False)
    chat_id = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    subscribed_until = Column(DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return f"<Tenant(id={self.id}, name={self.name}, chat_id={self.chat_id})>"