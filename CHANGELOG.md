# Changelog

## [1.1.0] - 2026-09-17
### Added
- BotHandler class (OOP refactor)
- Inline keyboard interaktif untuk menu produk
- FAQ berbasis keyword dengan multiple response
- Fallback untuk pertanyaan di luar topik
- File .gitignore yang benar

### Security
- Revoke token Telegram yang ter-expose
- Ganti nama file.gitignore → .gitignore
- Hapus .env dari Git tracking
- Rebuild repo GitHub dengan history bersih

### Fixed
- File handler.py yang kosong (3 bytes → 13 KB)
- Restore project dari backup flashdisk
- Sinkronisasi folder kerja dengan folder Git

## [1.0.0] - 2026-08-05
### Added
- Telegram Bot dengan command /start dan /help
- Fitur FAQ, Produk, Jam Operasional, Kontak
- Multi-tenant architecture (basic)
- Logging system
- Virtual environment