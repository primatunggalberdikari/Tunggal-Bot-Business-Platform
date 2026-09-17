"""
Handler utama untuk Telegram Bot.
Mengelola start/stop bot dan routing pesan.
Menggunakan OOP dengan class BotHandler.
"""

import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

from config.settings import settings

# Setup logging
logger = logging.getLogger(__name__)


class BotHandler:
    """
    Class handler untuk Telegram Bot.
    Menerapkan prinsip Single Responsibility - hanya menangani bot.
    """

    # Fallback untuk pertanyaan di luar topik
    FALLBACK_DILUAR_TOPIK = (
        "ini adalah pertanyaan yang sangat menarik dan sayangnya "
        "saya adalah assisten online untuk menjual produk anda"
    )

    def __init__(self):
        """Inisialisasi bot handler."""
        self._application: Application | None = None
        self._is_running: bool = False

    @property
    def is_running(self) -> bool:
        """Cek apakah bot sedang berjalan."""
        return self._is_running

    # ============================================================
    # BUILD APPLICATION
    # ============================================================
    def _build_application(self) -> Application:
        """Membangun aplikasi Telegram dengan semua handler."""
        app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", self._start_command))
        app.add_handler(CommandHandler("help", self._help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))
        app.add_handler(CallbackQueryHandler(self._button_click))
        app.add_error_handler(self._error_handler)

        return app

    # ============================================================
    # COMMAND /start
    # ============================================================
    async def _start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handler untuk command /start."""
        nama = update.effective_user.first_name or "Kak"
        await update.message.reply_text(
            f"Halo *{nama}*! 👋\n\n"
            "Selamat datang di *Tunggal Bot Bisnis* — asisten AI yang siap bantu "
            "bisnis Anda tumbuh 24 jam nonstop! 🤖\n\n"
            "Saya bisa bantu Anda:\n"
            "• Lihat produk & harga → ketik `produk`\n"
            "• Tanya apa saja soal layanan → ketik `faq`\n"
            "• Cek jam operasional → ketik `jam`\n"
            "• Hubungi admin → ketik `kontak`\n\n"
            "Ketik /help untuk daftar lengkap perintah.\n"
            "Yuk, mulai! Mau tanya apa hari ini? 😊",
            parse_mode="Markdown",
        )

    # ============================================================
    # COMMAND /help
    # ============================================================
    async def _help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handler untuk command /help."""
        await update.message.reply_text(
            "📋 *Perintah yang tersedia:*\n"
            "/start — Mulai bot\n"
            "/help — Bantuan ini\n\n"
            "🤖 *Menu Layanan AI Kami:*\n"
            "• `produk` — Lihat semua produk & harga\n"
            "• `faq` — Pertanyaan umum\n"
            "• `jam` — Jam operasional\n"
            "• `kontak` — Info kontak admin\n\n"
            "💡 *Tips:* Anda juga bisa langsung mengetik pertanyaan!",
            parse_mode="Markdown",
        )

    # ============================================================
    # MENU PRODUK INTERAKTIF
    # ============================================================
    async def _show_product_menu(self, update: Update) -> None:
        """Menampilkan menu produk dengan tombol interaktif."""
        keyboard = [
            [
                InlineKeyboardButton("📦 Integrasi Telegram", callback_data='detail_telegram'),
                InlineKeyboardButton("📦 Integrasi WhatsApp", callback_data='detail_wa'),
            ],
            [
                InlineKeyboardButton("🚀 Paket Combo", callback_data='detail_keduanya'),
                InlineKeyboardButton("🎧 Discord Server", callback_data='detail_discord'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "🤖 *Layanan AI Kami — Siap Membantu Bisnis Anda!*\n\n"
            "👇 *Klik tombol di bawah untuk melihat detail & harga:*",
            reply_markup=reply_markup,
            parse_mode="Markdown",
        )

    # ============================================================
    # CALLBACK BUTTON
    # ============================================================
    async def _button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handler untuk tombol yang diklik."""
        query = update.callback_query
        await query.answer()

        if query.data == 'detail_telegram':
            text = (
                "🤖 *AI Assistant untuk Telegram*\n"
                "💰 Harga: Rp 150.000/bulan\n\n"
                "Mau order? Ketik `kontak` untuk hubungi admin! 😊"
            )
        elif query.data == 'detail_wa':
            text = (
                "🤖 *AI Assistant untuk WhatsApp*\n"
                "💰 Harga: Rp 150.000/bulan\n\n"
                "Tertarik? Ketik `kontak` untuk mulai order! 🛒"
            )
        elif query.data == 'detail_keduanya':
            text = (
                "🚀 *Paket Combo AI — Telegram + WhatsApp*\n"
                "💰 Harga Spesial: Rp 200.000/bulan\n\n"
                "Ambil paket ini? Ketik `kontak` sekarang! ⚡"
            )
        elif query.data == 'detail_discord':
            text = (
                "🎧 *AI Building Discord Server*\n"
                "💰 Harga: Rp 150.000/bulan\n\n"
                "Mau bikin server impianmu? Ketik `kontak` ya! 🎮"
            )
        else:
            text = "Tombol tidak dikenali."

        await query.edit_message_text(text=text, parse_mode="Markdown")

    # ============================================================
    # FAQ AI BERBASIS KEYWORD
    # ============================================================
    async def _handle_faq_ai(self, update: Update, text: str) -> None:
        """Menangani FAQ berdasarkan kata kunci."""
        if any(k in text for k in ['order', 'pesan', 'beli', 'pesanan', 'pembelian']):
            response = (
                "Siap! 🛒 Caranya gampang banget:\n"
                "1. Ketik `produk`\n"
                "2. Pilih layanan favoritmu\n"
                "3. Ikuti instruksi pembayaran\n\n"
                "Mau saya bantu pilihkan yang paling cocok?"
            )
        elif any(k in text for k in ['bayar', 'transfer', 'pembayaran', 'rekening']):
            response = (
                "Pembayaran fleksibel, kok! 💳\n"
                "• Transfer Bank: BCA / Mandiri\n"
                "• E-Wallet: GoPay / OVO / Dana\n\n"
                "Bukti transfer tinggal kirim ke admin ya. Aman & tercatat!"
            )
        elif any(k in text for k in ['aman', 'keamanan', 'percaya', 'garansi', 'privasi']):
            response = (
                "100% aman! 🔒 Data Anda terenkripsi, transaksi tercatat, "
                "dan kami punya garansi uang kembali jika tidak sesuai."
            )
        elif any(k in text for k in ['cara', 'pakai', 'gunakan', 'tutorial', 'panduan']):
            response = (
                "Gampang banget! 📘 Setelah produk jadi, kami kirim:\n"
                "• Panduan step-by-step\n"
                "• Video tutorial\n"
                "• Support 3 hari pertama\n\n"
                "Dijamin langsung bisa pakai!"
            )
        elif any(k in text for k in ['produk', 'layanan', 'jasa', 'ai', 'bot', 'telegram', 'whatsapp', 'discord']):
            response = (
                "🤖 *Kami menyediakan layanan AI berikut:*\n"
                "• Integrasi Telegram\n"
                "• Integrasi WhatsApp\n"
                "• Paket Combo (keduanya)\n"
                "• Building Discord Server\n\n"
                "Ketik `produk` untuk lihat detail & harga ya! 👇"
            )
        else:
            response = self.FALLBACK_DILUAR_TOPIK

        await update.message.reply_text(response, parse_mode="Markdown")

    # ============================================================
    # HANDLE MESSAGE
    # ============================================================
    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handler untuk pesan teks biasa."""
        text = update.message.text.lower().strip()

        # Sapaan
        if text in ['hai', 'hi', 'halo', 'hello', 'hallo', 'pagi', 'siang', 'sore', 'malam', 'assalamualaikum', 'permisi']:
            nama = update.effective_user.first_name or "Kak"
            await update.message.reply_text(
                f"Halo *{nama}*! 👋 Selamat datang di *Tunggal Bot Bisnis*!\n\n"
                "Mau ngapain hari ini?\n"
                "• Ketik `produk` — lihat layanan AI kami\n"
                "• Ketik `faq` — tanya apa saja\n"
                "• Ketik `kontak` — hubungi admin",
                parse_mode="Markdown",
            )

        elif text == 'produk':
            await self._show_product_menu(update)

        elif text == 'faq':
            await update.message.reply_text(
                "❓ *Pertanyaan Umum (FAQ):*\n\n"
                "Silakan tanyakan apa saja, contoh:\n"
                "• Bagaimana cara order?\n"
                "• Bagaimana cara membayarnya?\n"
                "• Apakah layanan ini aman?\n\n"
                "Ketik pertanyaan Anda sekarang! 💬",
                parse_mode="Markdown",
            )

        elif text == 'jam':
            await update.message.reply_text(
                "🕒 *Jam Operasional Kami:*\n"
                "Senin – Kamis: 09.00 – 17.00 WIB\n"
                "Jumat & Minggu: Tutup (Libur).\n\n"
                "Tapi tenang, bot AI ini aktif 24 jam! 🤖",
                parse_mode="Markdown",
            )

        elif text == 'kontak':
            await update.message.reply_text(
                "📞 *Hubungi Kami:*\n"
                "📱 WhatsApp: 0882-9468-9521\n"
                "📧 Email: primatunggalberdikari@gmail.com\n\n"
                "🔗 Telegram: https://t.me/prima_tunggal_bot\n"
                "⏱️ Balas cepat maksimal 1x24 jam.",
                parse_mode="Markdown",
            )

        else:
            await self._handle_faq_ai(update, text)

    # ============================================================
    # ERROR HANDLER
    # ============================================================
    async def _error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handler untuk error."""
        logger.error(f"Error di bot: {context.error}")
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "Maaf, terjadi kesalahan. Tim kami akan segera memperbaikinya."
            )

    # ============================================================
    # START & STOP
    # ============================================================
    def start(self) -> None:
        """Memulai bot Telegram."""
        if self._is_running:
            logger.warning("Bot sudah berjalan!")
            return

        logger.info("Memulai bot Telegram...")
        self._application = self._build_application()
        logger.info("Bot mulai polling...")
        self._application.run_polling()
        self._is_running = True

    def stop(self) -> None:
        """Menghentikan bot Telegram."""
        if not self._is_running:
            logger.warning("Bot tidak sedang berjalan!")
            return

        logger.info("Menghentikan bot Telegram...")
        if self._application:
            self._application.stop()
        self._is_running = False
        logger.info("Bot berhasil dihentikan.")


# Instance handler untuk digunakan di main.py
bot_handler = BotHandler()


# Fungsi wrapper untuk kompatibilitas dengan main.py
def run_bot() -> None:
    """Fungsi wrapper untuk memulai bot."""
    bot_handler.start()


def stop() -> None:
    """Fungsi wrapper untuk menghentikan bot."""
    bot_handler.stop()