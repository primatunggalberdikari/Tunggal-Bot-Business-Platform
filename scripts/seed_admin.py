"""
Skrip seed admin pertama ke database.
Jalankan sekali setelah setup database.

Cara pakai:
    python scripts/seed_admin.py
"""

import sys
import logging
from pathlib import Path

# Tambahkan root project ke sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from database.connection import db_manager
from models.admin import Admin

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================
# Data admin yang akan dibuat
# ============================================================
ADMIN_DATA = {
    'username': 'admin',
    'email': 'admin@primatunggalberdikari.com',
    'password': 'admin123',
    'full_name': 'Super Admin',
    'is_super_admin': True,
}


def main() -> None:
    """Fungsi utama seed admin."""
    print("=" * 60)
    print("  SEED ADMIN")
    print("  Tunggal Bot Business Platform")
    print("=" * 60)

    # Buat tabel jika belum ada
    print("\n[Step 1] Memastikan tabel database sudah ada...")
    db_manager.create_tables()
    print("  OK: Tabel siap.")

    # Buka session
    print("\n[Step 2] Membuka session database...")
    session = db_manager.get_session()
    print("  OK: Session terbuka.")

    try:
        # Cek apakah admin sudah ada
        print("\n[Step 3] Cek admin yang ada di database...")
        existing_admin = session.query(Admin).filter(
            Admin.username == ADMIN_DATA['username']
        ).first()

        if existing_admin:
            print(f"  INFO: Admin '{ADMIN_DATA['username']}' sudah ada. Skip.")
            print(f"  Admin ID: {existing_admin.id}")
            print(f"  Email: {existing_admin.email}")
        else:
            # Buat admin baru
            print(f"\n[Step 4] Membuat admin baru: {ADMIN_DATA['username']}...")
            admin = Admin(
                username=ADMIN_DATA['username'],
                email=ADMIN_DATA['email'],
                full_name=ADMIN_DATA['full_name'],
                is_super_admin=ADMIN_DATA['is_super_admin'],
                is_active=True,
            )
            # Hash password sebelum simpan
            admin.set_password(ADMIN_DATA['password'])
            session.add(admin)
            session.commit()
            session.refresh(admin)

            print(f"  OK: Admin berhasil dibuat!")
            print(f"  Admin ID: {admin.id}")
            print(f"  Username: {admin.username}")
            print(f"  Email: {admin.email}")
            print(f"  Password: {ADMIN_DATA['password']} (di-hash di database)")
            print(f"  Super Admin: {admin.is_super_admin}")

    except Exception as e:
        logger.error(f"Error saat seed admin: {e}", exc_info=True)
        session.rollback()
        print(f"\n  ERROR: {e}")
    finally:
        session.close()
        print("\n  Session ditutup.")

    print("\n" + "=" * 60)
    print("  SEED ADMIN SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    main()