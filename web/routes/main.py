"""
Routes utama untuk web dashboard.
Menangani halaman landing, about, product, contact.
"""

from flask import Blueprint, render_template

# Buat Blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def landing():
    """Halaman landing dengan form pendaftaran."""
    return render_template('landing.html')


@main_bp.route('/about')
def about():
    """Halaman tentang perusahaan."""
    return render_template('landing.html')  # Sementara redirect ke landing


@main_bp.route('/product')
def product():
    """Halaman produk."""
    return render_template('landing.html')  # Sementara redirect ke landing


@main_bp.route('/contact')
def contact():
    """Halaman kontak."""
    return render_template('landing.html')  # Sementara redirect ke landing