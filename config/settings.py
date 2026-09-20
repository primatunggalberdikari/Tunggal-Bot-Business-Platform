"""
Konfigurasi software Tunggal Bot Business Platform.
Menggunakan python-dotenv untuk membaca environment variable.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Tentukan path untuk root project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from file .env
load_dotenv(BASE_DIR / '.env')


class Settings:
    """Class konfigurasi utama software."""

    # === Bot for Telegram === #
    TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN', '')

    # === Software for Bot === #
    APP_NAME: str = os.getenv('APP_NAME', 'Tunggal Bot Business Platform')
    APP_ENV: str = os.getenv('APP_ENV', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'True').lower() == 'true'

    # === SYSTEM DATABASE === #
    DATABASE_URL: str = os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR}/tunggal_bot.db')

        # === Flask Web ===
    FLASK_SECRET_KEY: str = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-this')
    FLASK_DEBUG: bool = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    @property
    def is_production(self) -> bool:
        """Cek apakah software berjalan di mode production."""
        return self.APP_ENV.lower() == 'production'

    @property
    def is_development(self) -> bool:
        """Cek apakah software berjalan di mode development."""
        return self.APP_ENV.lower() == 'development'

    def validate(self) -> bool:
        """Validasi konfigurasi sebelum software berjalan."""
        if not self.TELEGRAM_BOT_TOKEN:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN tidak ditemukan! "
                "Silakan set di file .env"
            )
        return True

# Instance settings yang bisa di-import di seluruh software
settings = Settings()