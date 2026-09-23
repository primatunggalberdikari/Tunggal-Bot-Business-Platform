"""
Routes utama untuk web dashboard.
Menangani halaman landing, about, product, contact.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def landing():
    """Halaman landing dengan form pendaftaran."""
    return render_template('landing.html')


@main_bp.route('/register', methods=['POST'])
def register():
    """Handle form pendaftaran (sementara hanya print)."""
    nama = request.form.get('nama')
    email = request.form.get('email')
    hp = request.form.get('hp')
    alamat = request.form.get('alamat')
    password = request.form.get('password')
    konfirmasi = request.form.get('konfirmasi_password')
    syarat = request.form.get('syarat')
    
    # Validasi sederhana
    if not nama or not email or not password:
        flash('Semua field wajib diisi!', 'error')
        return redirect(url_for('main.landing'))
    
    if password != konfirmasi:
        flash('Password dan konfirmasi tidak sama!', 'error')
        return redirect(url_for('main.landing'))
    
    if not syarat:
        flash('Anda harus menyetujui syarat & ketentuan!', 'error')
        return redirect(url_for('main.landing'))
    
    # Sementara: print ke console
    print(f"=== PENDAFTARAN BARU ===")
    print(f"Nama: {nama}")
    print(f"Email: {email}")
    print(f"HP: {hp}")
    print(f"Alamat: {alamat}")
    
    flash(f'Pendaftaran berhasil, {nama}! (sementara belum disimpan)', 'success')
    return redirect(url_for('main.landing'))


@main_bp.route('/about')
def about():
    """Halaman tentang perusahaan."""
    return render_template('landing.html')


@main_bp.route('/product')
def product():
    """Halaman produk."""
    return render_template('landing.html')


@main_bp.route('/contact')
def contact():
    """Halaman kontak."""
    return render_template('landing.html')