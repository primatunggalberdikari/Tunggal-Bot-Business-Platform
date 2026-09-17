"""
Model untuk Kontak.
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class Contact(BaseModel):
    """Model untuk menyimpan kontak UMKM."""
    __tablename__ = "contacts"

    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    type = Column(String(20), nullable=False)   # phone, email, address, social
    value = Column(String(200), nullable=False)
    label = Column(String(50), nullable=True)
    order = Column(Integer, default=0)

    tenant = relationship("Tenant", backref="contacts")

    def __repr__(self) -> str:
        return f"<Contact(id={self.id}, type={self.type}, value={self.value})>"