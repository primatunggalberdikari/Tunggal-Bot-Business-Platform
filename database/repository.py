"""
Repository untuk akses database.
Mengimplementasikan pattern Repository untuk memisahkan logika database.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from models.tenant import Tenant
from models.product import Product
from models.faq import FAQ
from models.business_hours import BusinessHours
from models.contact import Contact
from models.chat_log import ChatLog
from database.connection import db_manager


class TenantRepository:
    """Repository untuk operasi database terkait Tenant."""
    
    def __init__(self):
        self._session: Session = db_manager.get_session()
    
    def get_by_chat_id(self, chat_id: str) -> Optional[Tenant]:
        """Mencari tenant berdasarkan chat_id."""
        return self._session.query(Tenant).filter(Tenant.chat_id == chat_id).first()
    
    def get_or_create(self, chat_id: str, name: str = "UMKM") -> Tenant:
        """Mendapatkan tenant atau membuat baru jika belum ada."""
        tenant = self.get_by_chat_id(chat_id)
        if tenant is None:
            tenant = Tenant(chat_id=chat_id, name=name)
            self._session.add(tenant)
            self._session.commit()
            self._session.refresh(tenant)
        return tenant
    
    def get_active_tenants(self) -> List[Tenant]:
        """Mendapatkan semua tenant yang aktif."""
        return self._session.query(Tenant).filter(Tenant.is_active == True).all()
    
    def close(self):
        """Menutup session."""
        self._session.close()


class ProductRepository:
    """Repository untuk operasi database terkait Product."""
    
    def __init__(self):
        self._session: Session = db_manager.get_session()
    
    def get_by_tenant(self, tenant_id: int) -> List[Product]:
        """Mendapatkan semua produk dari tenant tertentu."""
        return self._session.query(Product).filter(
            Product.tenant_id == tenant_id,
            Product.is_active == True
        ).all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Mendapatkan produk berdasarkan ID."""
        return self._session.query(Product).filter(Product.id == product_id).first()
    
    def close(self):
        """Menutup session."""
        self._session.close()


class FAQRepository:
    """Repository untuk operasi database terkait FAQ."""
    
    def __init__(self):
        self._session: Session = db_manager.get_session()
    
    def get_by_tenant(self, tenant_id: int) -> List[FAQ]:
        """Mendapatkan semua FAQ dari tenant tertentu."""
        return self._session.query(FAQ).filter(
            FAQ.tenant_id == tenant_id,
            FAQ.is_active == True
        ).order_by(FAQ.order).all()
    
    def close(self):
        """Menutup session."""
        self._session.close()