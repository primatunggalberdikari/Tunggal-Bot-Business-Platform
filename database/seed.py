"""
Seed data untuk database.
Mengisi database dengan data contoh untuk tenant baru.
"""

import logging
from sqlalchemy.orm import Session

from models.tenant import Tenant
from models.product import Product
from models.faq import FAQ
from models.business_hours import BusinessHours
from models.contact import Contact

logger = logging.getLogger(__name__)


class DatabaseSeeder:
    """Class untuk mengisi database dengan data contoh."""

    def __init__(self, session: Session):
        """
        Inisialisasi seeder.
        
        Args:
            session: SQLAlchemy session untuk operasi database.
        """
        self._session = session

    def seed_default_data(self, tenant: Tenant) -> None:
        """
        Isi data contoh untuk tenant baru.
        
        Args:
            tenant: Instance Tenant yang akan diisi data contoh.
        """
        logger.info(f"Seed data untuk tenant: {tenant.name}")
        
        self._seed_products(tenant)
        self._seed_faqs(tenant)
        self._seed_business_hours(tenant)
        self._seed_contacts(tenant)
        
        self._session.commit()
        logger.info(f"Seed data selesai untuk tenant: {tenant.name}")

    def _seed_products(self, tenant: Tenant) -> None:
        """Isi produk contoh."""
        products = [
            Product(
                tenant_id=tenant.id,
                name="AI Assistant Telegram",
                description="Bot AI otomatis 24 jam untuk Telegram",
                price=150000,
                stock=999,
                category="Layanan AI",
                is_active=True,
            ),
            Product(
                tenant_id=tenant.id,
                name="AI Assistant WhatsApp",
                description="Balas otomatis WA dengan AI",
                price=150000,
                stock=999,
                category="Layanan AI",
                is_active=True,
            ),
            Product(
                tenant_id=tenant.id,
                name="Paket Combo Telegram + WhatsApp",
                description="Semua fitur AI di kedua platform",
                price=200000,
                stock=999,
                category="Paket",
                is_active=True,
            ),
            Product(
                tenant_id=tenant.id,
                name="Building Discord Server",
                description="Server Discord siap pakai dengan bot AI",
                price=150000,
                stock=999,
                category="Layanan AI",
                is_active=True,
            ),
        ]
        for product in products:
            self._session.add(product)

    def _seed_faqs(self, tenant: Tenant) -> None:
        """Isi FAQ contoh."""
        faqs = [
            FAQ(
                tenant_id=tenant.id,
                question="Bagaimana cara order?",
                answer="Ketik 'produk', pilih layanan, lalu ketik 'kontak' untuk hubungi admin.",
                order=1,
                is_active=True,
            ),
            FAQ(
                tenant_id=tenant.id,
                question="Bagaimana cara membayar?",
                answer="Transfer Bank (BCA/Mandiri) atau E-Wallet (GoPay/OVO/Dana).",
                order=2,
                is_active=True,
            ),
            FAQ(
                tenant_id=tenant.id,
                question="Apakah layanan ini aman?",
                answer="100% aman. Data terenkripsi, ada garansi uang kembali.",
                order=3,
                is_active=True,
            ),
            FAQ(
                tenant_id=tenant.id,
                question="Berapa lama proses pembuatan?",
                answer="1-3 hari kerja setelah pembayaran dikonfirmasi.",
                order=4,
                is_active=True,
            ),
        ]
        for faq in faqs:
            self._session.add(faq)

    def _seed_business_hours(self, tenant: Tenant) -> None:
        """Isi jam operasional contoh (Senin-Minggu)."""
        hours_data = [
            (0, "09:00", "17:00", False),
            (1, "09:00", "17:00", False),
            (2, "09:00", "17:00", False),
            (3, "09:00", "17:00", False),
            (4, "09:00", "17:00", False),
            (5, "10:00", "15:00", False),
            (6, None, None, True),
        ]
        for day, open_time, close_time, is_closed in hours_data:
            bh = BusinessHours(
                tenant_id=tenant.id,
                day_of_week=day,
                open_time=open_time,
                close_time=close_time,
                is_closed=is_closed,
            )
            self._session.add(bh)

    def _seed_contacts(self, tenant: Tenant) -> None:
        """Isi kontak contoh."""
        contacts = [
            Contact(
                tenant_id=tenant.id,
                type="whatsapp",
                value="0882-9468-9521",
                label="WhatsApp",
                order=1,
            ),
            Contact(
                tenant_id=tenant.id,
                type="email",
                value="primatunggalberdikari@gmail.com",
                label="Email",
                order=2,
            ),
            Contact(
                tenant_id=tenant.id,
                type="telegram",
                value="https://t.me/prima_tunggal_bot",
                label="Telegram",
                order=3,
            ),
        ]
        for contact in contacts:
            self._session.add(contact)