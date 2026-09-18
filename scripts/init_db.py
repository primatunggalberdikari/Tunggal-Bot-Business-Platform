"""
Skrip inisialisasi database.
Jalankan sekali untuk membuat tabel dan cek data seed.

Cara pakai:
    python scripts/init_db.py
"""

import sys
import logging
from pathlib import Path

# Tambahkan root project ke sys.path agar bisa import config, models, dll.
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from database.connection import db_manager
from models.tenant import Tenant

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Fungsi utama inisialisasi database."""
    print("=" * 60)
    print("  INISIALISASI DATABASE")
    print("  Tunggal Bot Business Platform")
    print("=" * 60)

    # Step 1: Buat semua tabel
    print("\n[Step 1] Membuat tabel database...")
    logger.info("Membuat tabel database...")
    db_manager.create_tables()
    logger.info("Tabel berhasil dibuat / sudah ada.")
    print("  OK: Tabel siap.")

    # Step 2: Cek tenant yang ada
    print("\n[Step 2] Cek tenant yang ada di database...")
    session = db_manager.get_session()
    try:
        tenant_count = session.query(Tenant).count()
        print(f"  Jumlah tenant saat ini: {tenant_count}")

        if tenant_count == 0:
            print("\n[Step 3] Belum ada tenant.")
            print("  Seed data akan otomatis dibuat saat user /start.")
        else:
            print("\n[Step 3] Daftar tenant:")
            tenants = session.query(Tenant).all()
            for t in tenants:
                print(f"    - [{t.id}] {t.name} (chat_id: {t.chat_id})")
    finally:
        session.close()

    print("\n" + "=" * 60)
    print("  INISIALISASI SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    main()