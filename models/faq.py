"""
Model untuk FAQ.
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class FAQ(BaseModel):
    """Model untuk menyimpan FAQ UMKM."""
    __tablename__ = "faqs"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    question = Column(String(200), nullable=False)
    answer = Column(String(1000), nullable=False)
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    
    tenant = relationship("Tenant", backref="faqs")
    
    def __repr__(self) -> str:
        return f"<FAQ(id={self.id}, question={self.question[:30]})>"