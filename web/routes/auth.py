"""
Routes untuk autentikasi: login, logout.
Sementara menggunakan kredensial hardcode (belum database).
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

auth_bp = Blueprint('auth', __name__)


# ============================================================
# Kredensial dummy — nanti diganti dengan database
# ============================================================
DUMMY_USERNAME = 'admin'
DUMMY_PASSWORD = 'admin123'


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

        # Cek kredensial dummy
        if username == DUMMY_USERNAME and password == DUMMY_PASSWORD:
            # Login sukses
            session['user'] = username
            session['is_admin'] = True

            if remember:
                session.permanent = True

            flash(f'Selamat datang, {username}!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            # Login gagal
            flash('Username atau password salah!', 'error')
            return redirect(url_for('auth.login'))

    # GET request — tampilkan form login
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    """Logout dan hapus session."""
    username = session.get('user', 'User')
    session.clear()
    flash(f'Anda telah logout, {username}.', 'info')
    return redirect(url_for('main.landing'))


@auth_bp.route('/dashboard')
def dashboard():
    """Halaman dashboard admin (sederhana)."""
    # Cek login
    if not session.get('user'):
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html', username=session.get('user'))