"""
Model untuk Jam Operasional.
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Time
from sqlalchemy.orm import relationship
from .base import BaseModel


class BusinessHours(BaseModel):
    """Model untuk menyimpan jam operasional UMKM."""
    __tablename__ = "business_hours"

    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    day_of_week = Column(Integer, nullable=False)  # 0=Senin, 6=Minggu
    open_time = Column(String(5), nullable=True)   # Format: "08:00"
    close_time = Column(String(5), nullable=True)  # Format: "20:00"
    is_closed = Column(Boolean, default=False)

    tenant = relationship("Tenant", backref="business_hours")

    def __repr__(self) -> str:
        return f"<BusinessHours(id={self.id}, day={self.day_of_week})>"