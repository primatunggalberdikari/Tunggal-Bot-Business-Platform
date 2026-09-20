# Changelog

## [1.1.0] - 2026-09-19
### Added
- SQLite database integration with SQLAlchemy
- 6 database models (Tenant, Product, FAQ, BusinessHours, Contact, ChatLog)
- Repository Pattern untuk akses database
- Multi-tenant: setiap user = 1 tenant dengan chat_id unik
- Seed data otomatis saat tenant baru /start
- Bot ambil produk dari database (bukan hardcode)
- Bot ambil FAQ dari database
- Bot ambil jam operasional dari database
- Bot ambil kontak dari database
- Logging percakapan ke database (chat_logs)
- Intent classification (produk, faq, jam, kontak, sapaan, faq_ai)

### Fixed
- SQLAlchemy compatibility with Python 3.13
- Missing tables due to unregistered models
- Indentation issues in handler methods

## [1.0.0] - 2026-08-05
### Added
- Telegram Bot dengan command /start dan /help
- Fitur FAQ, Produk, Jam Operasional, Kontak
- Logging system
- Virtual environment