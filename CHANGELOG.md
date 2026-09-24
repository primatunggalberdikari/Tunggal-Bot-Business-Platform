# Changelog

## [2.0.0-dev] - 2026-09-23
### Added
- Landing page dengan template inheritance (`base.html`)
- Halaman login admin dengan session management
- Halaman dashboard admin (sederhana)
- Static files management (`base.css`, `base.js`)
- Flash messages untuk notifikasi
- Navbar dinamis (login/logout state)
- Route `/login`, `/logout`, `/dashboard`
- Blueprint `auth_bp` untuk autentikasi
- Kredensial dummy (admin/admin123) untuk testing

### Changed
- Refactor `landing.html` — extends `base.html`
- Hapus folder root `templates/` (bersih)
- Update `web/__init__.py` — register `auth_bp`

### Security
- Session-based authentication
- Password akan di-hash (persiapan V3.0)

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