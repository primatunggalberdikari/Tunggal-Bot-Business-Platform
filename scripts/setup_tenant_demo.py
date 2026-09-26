"""
Skrip setup tenant demo untuk testing.
Membuat 1 tenant + set admin ke tenant tersebut.

Cara pakai:
    python scripts/setup_tenant_demo.py
"""

import sys
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from database.connection import db_manager
from models.tenant import Tenant
from models.admin import Admin

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================
# Data tenant demo
# ============================================================
TENANT_DATA = {
    'name': 'Toko Demo',
    'chat_id': 'demo_chat_001',
    'description': 'Tenant untuk testing CRUD',
    'is_active': True,
}

ADMIN_USERNAME = 'admin'


def main() -> None:
    """Fungsi utama setup tenant demo."""
    print("=" * 60)
    print("  SETUP TENANT DEMO")
    print("  Tunggal Bot Business Platform")
    print("=" * 60)

    session = db_manager.get_session()
    try:
        # Step 1: Cek/buat tenant
        print("\n[Step 1] Cek tenant demo...")
        tenant = session.query(Tenant).filter(
            Tenant.chat_id == TENANT_DATA['chat_id']
        ).first()

        if tenant:
            print(f"  INFO: Tenant '{tenant.name}' sudah ada. Skip.")
        else:
            print(f"  Membuat tenant baru: {TENANT_DATA['name']}...")
            tenant = Tenant(
                name=TENANT_DATA['name'],
                chat_id=TENANT_DATA['chat_id'],
                description=TENANT_DATA['description'],
                is_active=TENANT_DATA['is_active'],
            )
            session.add(tenant)
            session.commit()
            session.refresh(tenant)
            print(f"  OK: Tenant ID = {tenant.id}")

        # Step 2: Update admin
        print(f"\n[Step 2] Update admin '{ADMIN_USERNAME}'...")
        admin = session.query(Admin).filter(
            Admin.username == ADMIN_USERNAME
        ).first()

        if not admin:
            print(f"  ERROR: Admin '{ADMIN_USERNAME}' tidak ditemukan.")
            print(f"  Jalankan dulu: python scripts/seed_admin.py")
            return

        if admin.tenant_id == tenant.id:
            print(f"  INFO: Admin sudah punya tenant_id = {tenant.id}. Skip.")
        else:
            admin.tenant_id = tenant.id
            session.commit()
            print(f"  OK: Admin '{admin.username}' → tenant_id = {tenant.id}")

        # Step 3: Verifikasi
        print(f"\n[Step 3] Verifikasi...")
        print(f"  Tenant ID: {tenant.id} ({tenant.name})")
        print(f"  Admin tenant_id: {admin.tenant_id}")

    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        session.rollback()
        print(f"\n  ERROR: {e}")
    finally:
        session.close()

    print("\n" + "=" * 60)
    print("  SETUP TENANT DEMO SELESAI")
    print("=" * 60)
    print("\nLangkah selanjutnya:")
    print("  1. Logout dari aplikasi (kalau sedang login)")
    print("  2. Login ulang dengan admin/admin123")
    print("  3. Buka http://127.0.0.1:5000/products/")
    print("  4. Harusnya muncul 'tenant_id=1'")


if __name__ == "__main__":
    main()