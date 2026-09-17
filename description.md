# Tunggal Bot Bussiness Platform

**PRIMA TUNGGAL BERDIKARI**
*"SOFTWARE LOKAL DENGAN INOVASI GLOBAL"*

## Deskripsi
Tunggal Bot adalah platform Chatbot Multi-Tenant berbasis Python untuk UMKM. 
1 kode sistem dapat melayani banyak klien secara bersamaan dengan data yang terpisah. 
Fitur utama meliputi Auto Reply 24 Jam, Ambil Pesanan Otomatis, Jam Kerja, dan Kontak CS. 
Dirancang untuk membantu UMKM meningkatkan layanan pelanggan tanpa perlu tim CS tambahan.

## Teknologi
-Python 3.11+
-Python-telegram-bot
-Botpress
-Midtrans
-Flask
-SQLite/PostgreSQL
-SQLalchemy

## Struktur Project

Tunggal-Bot-Business-Platform/
│
├── bot/                        # Modul Telegram Bot
│   ├── __init__.py
│   ├── handler.py              # Handler pesan utama
│   ├── menu.py                 # Menu dan keyboard
│   └── callback.py             # Callback query handler
│
├── web/                        # Modul Dashboard Flask
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py             # Login/Logout
│   │   ├── dashboard.py        # Dashboard utama
│   │   └── products.py         # CRUD produk
│   └── templates/              # HTML Templates
│
├── models/                     # Database Models (SQLAlchemy)
│   ├── __init__.py
│   ├── tenant.py
│   ├── product.py
│   ├── faq.py
│   ├── business_hours.py
│   ├── contact.py
│   └── chat_log.py
│
├── database/                   # Database Layer
│   ├── __init__.py
│   ├── connection.py           # Koneksi database
│   ├── repository.py           # CRUD operations
│   └── migrations/             # Migration scripts
│
├── services/                   # Business Logic Layer
│   ├── __init__.py
│   ├── bot_service.py          # Service untuk bot
│   ├── tenant_service.py       # Service untuk tenant
│   └── analytics_service.py    # Service untuk statistik
│
├── config/                     # Konfigurasi
│   ├── __init__.py
│   ├── settings.py             # Pengaturan global
│   └── logging_config.py       # Konfigurasi logging
│
├── static/                     # Static files (Web)
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/                  # Flask Templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   └── products/
│
├── tests/                      # Unit Testing
│   ├── __init__.py
│   ├── test_models.py
│   └── test_bot.py
│
├── logs/                       # Log files
├── docs/                       # Dokumentasi
├── migrations/                 # SQLAlchemy migrations
│
├── .env.example                # Contoh environment variables
├── .gitignore
├── requirements.txt            # Python dependencies
├── README.md
├── CHANGELOG.md
├── LICENSE
└── main.py                     # Entry point aplikasi

## Roadmap
-v1.0: Telegram Bot (FAQ, Deskripsi & Ketersediaan Produk, Pengambilan & Penerimaan Pesanan Otomatis, Jam Kerja,Kontak) #masih memakai botpress agar data customer lebih aman karena saya masih belum mempelajari cybersecurity
-v1.1: SQlite, logging, statistik
-v2.0: Dashboard Flask
-v3.0: PostgreSQL, multi-umkm

## Cara install

## License
MIT