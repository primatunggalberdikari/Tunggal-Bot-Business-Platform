# Changelog

## [2.0.1] - 2026-09-26
### Added
- CRUD Produk lengkap (Create, Read, Update, Delete)
- Halaman Daftar Produk (`/products/`) dengan card layout
- Form Tambah Produk (`/products/new`) — universal template
- Form Edit Produk (`/products/<id>/edit`)
- Hapus Produk (`/products/<id>/delete`) — POST + konfirmasi
- Blueprint `products_bp` untuk modular routing
- Helper functions `get_current_tenant_id()`, `require_login()`
- Konfirmasi hapus dengan JavaScript
- Update Dashboard dengan statistik (produk, chat)
- Navbar dinamis (Produk, Dashboard, Logout)
- Empty state untuk list produk kosong

### Security
- Filter double (id + tenant_id) di edit dan delete
- POST method untuk hapus (cegah CSRF/prefetch)
- Validasi input di form produk

### Changed
- Dashboard tidak lagi placeholder — ada statistik
- Navbar link "Produk" muncul saat login

## [2.0.0-dev] - 2026-09-25
### Added
- Landing page dengan template inheritance (`base.html`)
- Halaman login admin dengan database authentication
- Halaman dashboard admin (sederhana)
- Static files management (`base.css`, `base.js`)
- Flash messages untuk notifikasi
- Navbar dinamis (login/logout state)
- Route `/login`, `/logout`, `/dashboard`
- Blueprint `auth_bp` untuk autentikasi
- Database seed untuk admin pertama
- Password hashing dengan scrypt (werkzeug)
- Helper function `get_admin_by_username()`
- Session management (user, admin_id, tenant_id, is_super_admin)
- Auto-hide flash messages (5 detik)
- Show/hide password toggle
- Conditional DEBUG mode untuk kredensial test

### Changed
- Refactor `landing.html` — extends `base.html`
- Hapus folder root `templates/` (bersih)
- Update `web/__init__.py` — register `auth_bp`
- Ganti dummy auth → database auth

### Security
- Password di-hash dengan scrypt
- Session-based authentication
- Cek admin `is_active` sebelum login
- Conditional test credentials (hanya di DEBUG mode)

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