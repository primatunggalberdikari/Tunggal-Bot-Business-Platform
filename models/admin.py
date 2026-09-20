"""
Model untuk Admin (klien yang login ke dashboard).
"""

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from .base import BaseModel


class Admin(BaseModel):
    """Model untuk admin/klien dashboard."""
    __tablename__ = "admins"

    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_super_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # Relasi ke Tenant (opsional, untuk admin yang punya UMKM)
    tenant = relationship("Tenant", backref="admins")

    def set_password(self, password: str) -> None:
        """Hash dan set password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifikasi password."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<Admin(id={self.id}, username={self.username})>"