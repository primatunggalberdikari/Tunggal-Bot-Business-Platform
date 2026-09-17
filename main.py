"""
Entry point utama software Tunggal Bot Business platform.
"""

import logging
from config.settings import settings
from bot.handler import run_bot, stop


def setup_logging() -> None:
    """
    Konfigurasi logging untuk aplikasi.
    """
    import os
    os.makedirs('logs', exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO if not settings.DEBUG else logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs/app.log', encoding='utf-8')
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info(f"{settings.APP_NAME} v1.0.0")
    logger.info(f"Mode: {settings.APP_ENV}")
    logger.info(f"Debug: {settings.DEBUG}")


def main() -> None:
    """
    Fungsi utama software.
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        settings.validate()
        logger.info("[OK] Konfigurasi valid")  # Ganti ✓ dengan [OK]
    except ValueError as e:
        logger.error(f"[ERROR] {e}")  # Ganti ✕ dengan [ERROR]
        return

    print("=" * 50)
    print(f" {settings.APP_NAME}")
    print("=" * 50)
    print(f" Mode: {settings.APP_ENV}")
    print(f" Debug: {settings.DEBUG}")
    print("=" * 50)
    print(" Bot akan berjalan... Tekan Ctrl + C untuk berhenti")
    print("=" * 50)

    try:
        run_bot()
    except KeyboardInterrupt:
        logger.info(" Bot dihentikan oleh user")
        stop()
    except Exception as e:
        logger.error(f"[ERROR] Error fatal: {e}")  # Ganti ✕ dengan [ERROR]
        stop()


if __name__ == "__main__":
    main()