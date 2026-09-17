"""
Model untuk Produk.
"""

from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class Product(BaseModel):
    """Model untuk menyimpan produk UMKM."""
    __tablename__ = "products"
    
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    category = Column(String(50), nullable=True)
    image_url = Column(String(200), nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relasi ke Tenant
    tenant = relationship("Tenant", backref="products")
    
    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"