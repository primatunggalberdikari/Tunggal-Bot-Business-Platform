"""
Routes untuk autentikasi: login, logout.
Menggunakan database untuk verifikasi admin.
"""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)

from database.connection import db_manager
from models.admin import Admin

auth_bp = Blueprint('auth', __name__)


# ============================================================
# Helper function
# ============================================================
def get_admin_by_username(username: str):
    """
    Ambil admin dari database berdasarkan username.
    
    Args:
        username: Username admin.
    
    Returns:
        Admin instance atau None jika tidak ditemukan.
    """
    session_db = db_manager.get_session()
    try:
        admin = session_db.query(Admin).filter(
            Admin.username == username
        ).first()
        return admin
    finally:
        session_db.close()


# ============================================================
# Route: Login
# ============================================================
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login admin."""
    # Jika sudah login, redirect ke dashboard
    if session.get('user'):
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember')

        # Validasi input
        if not username or not password:
            flash('Username dan password wajib diisi!', 'error')
            return redirect(url_for('auth.login'))

        # Cari admin di database
        admin = get_admin_by_username(username)

        # Validasi: admin ada atau tidak
        if admin is None:
            flash('Username atau password salah!', 'error')
            return redirect(url_for('auth.login'))

        # Validasi: admin aktif atau tidak
        if not admin.is_active:
            flash('Akun Anda dinonaktifkan. Hubungi admin.', 'error')
            return redirect(url_for('auth.login'))

        # Validasi: password benar atau tidak
        if not admin.check_password(password):
            flash('Username atau password salah!', 'error')
            return redirect(url_for('auth.login'))

        # Login sukses — set session
        session['user'] = admin.username
        session['admin_id'] = admin.id
        session['is_super_admin'] = admin.is_super_admin
        session['tenant_id'] = admin.tenant_id
        session['full_name'] = admin.full_name or admin.username

        if remember:
            session.permanent = True

        flash(f'Selamat datang, {admin.full_name or admin.username}!', 'success')
        return redirect(url_for('auth.dashboard'))

        # GET request — tampilkan form login
    from config.settings import settings
    return render_template('login.html', settings=settings)


# ============================================================
# Route: Logout
# ============================================================
@auth_bp.route('/logout')
def logout():
    """Logout dan hapus session."""
    username = session.get('user', 'User')
    session.clear()
    flash(f'Anda telah logout, {username}.', 'info')
    return redirect(url_for('main.landing'))


# ============================================================
# Route: Dashboard
# ============================================================
@auth_bp.route('/dashboard')
def dashboard():
    """Halaman dashboard admin."""
    # Cek login
    if not session.get('user'):
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    # Kirim data admin ke template
    admin_data = {
        'username': session.get('user'),
        'full_name': session.get('full_name'),
        'is_super_admin': session.get('is_super_admin'),
        'tenant_id': session.get('tenant_id'),
    }

    return render_template('dashboard.html', admin=admin_data)