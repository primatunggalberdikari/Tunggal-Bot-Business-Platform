"""
Routes untuk CRUD Produk.
Setiap route HARUS filter by tenant_id (multi-tenant isolation).
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
from models.product import Product

products_bp = Blueprint('products', __name__)


# ============================================================
# Helper function
# ============================================================
def get_current_tenant_id():
    """
    Ambil tenant_id dari session.
    
    Returns:
        int atau None jika belum login.
    """
    return session.get('tenant_id')


def require_login():
    """
    Cek apakah user sudah login.
    
    Returns:
        True jika sudah login, False jika belum.
    """
    return bool(session.get('user'))


# ============================================================
# Route: List Produk
# ============================================================
@products_bp.route('/')
def list_products():
    """Halaman daftar produk — diambil dari database."""
    # 1. Cek login
    if not require_login():
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    # 2. Ambil tenant_id dari session
    tenant_id = get_current_tenant_id()

    # 3. Query produk dari database (FILTER by tenant_id!)
    session_db = db_manager.get_session()
    try:
        products = session_db.query(Product).filter(
            Product.tenant_id == tenant_id
        ).order_by(Product.created_at.desc()).all()
    finally:
        session_db.close()

    # 4. Render template
    return render_template(
        'products/list.html',
        products=products,
    )


# ============================================================
# Route: Tambah Produk (GET & POST)
# ============================================================
@products_bp.route('/new', methods=['GET', 'POST'])
def new_product():
    """Form tambah produk baru."""
    # 1. Cek login
    if not require_login():
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    # 2. Ambil tenant_id dari session
    tenant_id = get_current_tenant_id()

    # 3. Handle POST (user submit form)
    if request.method == 'POST':
        # Ambil data dari form
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price_str = request.form.get('price', '0').strip()
        stock_str = request.form.get('stock', '0').strip()
        category = request.form.get('category', '').strip()

        # Validasi
        if not name or not price_str:
            flash('Nama dan harga wajib diisi!', 'error')
            return redirect(url_for('products.new_product'))

        try:
            price = float(price_str)
            stock = int(stock_str) if stock_str else 0
        except ValueError:
            flash('Harga dan stok harus berupa angka!', 'error')
            return redirect(url_for('products.new_product'))

        # Simpan ke database
        session_db = db_manager.get_session()
        try:
            product = Product(
                tenant_id=tenant_id,
                name=name,
                description=description or None,
                price=price,
                stock=stock,
                category=category or None,
                is_active=True,
            )
            session_db.add(product)
            session_db.commit()
            session_db.refresh(product)

            flash(f'Produk "{product.name}" berhasil ditambahkan!', 'success')
            return redirect(url_for('products.list_products'))
        except Exception as e:
            session_db.rollback()
            flash(f'Error: {e}', 'error')
            return redirect(url_for('products.new_product'))
        finally:
            session_db.close()

    # 4. GET — tampilkan form kosong
    return render_template(
        'products/form.html',
        title='Tambah Produk',
        subtitle='Isi detail produk baru',
        form_action=url_for('products.new_product'),
        submit_label='SIMPAN PRODUK',
        product=None,
    )



# ============================================================
# Route: Edit Produk (GET & POST)
# ============================================================
@products_bp.route('/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id: int):
    """Form edit produk existing."""
    # 1. Cek login
    if not require_login():
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    # 2. Ambil tenant_id dari session
    tenant_id = get_current_tenant_id()

    # 3. Query produk dengan FILTER DOUBLE (id + tenant_id)
    session_db = db_manager.get_session()
    try:
        product = session_db.query(Product).filter(
            Product.id == product_id,
            Product.tenant_id == tenant_id,  # ← KUNCI ISOLASI!
        ).first()
    finally:
        session_db.close()

    # 4. Produk tidak ketemu atau bukan milik tenant ini
    if product is None:
        flash('Produk tidak ditemukan atau bukan milik Anda.', 'error')
        return redirect(url_for('products.list_products'))

    # 5. Handle POST (user submit form)
    if request.method == 'POST':
        # Ambil data dari form
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price_str = request.form.get('price', '0').strip()
        stock_str = request.form.get('stock', '0').strip()
        category = request.form.get('category', '').strip()

        # Validasi
        if not name or not price_str:
            flash('Nama dan harga wajib diisi!', 'error')
            return redirect(url_for('products.edit_product', product_id=product_id))

        try:
            price = float(price_str)
            stock = int(stock_str) if stock_str else 0
        except ValueError:
            flash('Harga dan stok harus berupa angka!', 'error')
            return redirect(url_for('products.edit_product', product_id=product_id))

        # Update database
        session_db = db_manager.get_session()
        try:
            # Query ulang dengan filter tenant_id (safety)
            product = session_db.query(Product).filter(
                Product.id == product_id,
                Product.tenant_id == tenant_id,
            ).first()

            if product is None:
                flash('Produk tidak ditemukan.', 'error')
                return redirect(url_for('products.list_products'))

            # Update field
            product.name = name
            product.description = description or None
            product.price = price
            product.stock = stock
            product.category = category or None

            session_db.commit()
            flash(f'Produk "{product.name}" berhasil diupdate!', 'success')
            return redirect(url_for('products.list_products'))
        except Exception as e:
            session_db.rollback()
            flash(f'Error: {e}', 'error')
            return redirect(url_for('products.edit_product', product_id=product_id))
        finally:
            session_db.close()

    # 6. GET — tampilkan form terisi
    return render_template(
        'products/form.html',
        title='Edit Produk',
        subtitle=f'Mengubah produk: {product.name}',
        form_action=url_for('products.edit_product', product_id=product_id),
        submit_label='SIMPAN PERUBAHAN',
        product=product,
    )



# ============================================================
# Route: Hapus Produk (POST)
# ============================================================
@products_bp.route('/<int:product_id>/delete', methods=['POST'])
def delete_product(product_id: int):
    """Hapus produk berdasarkan ID."""
    # 1. Cek login
    if not require_login():
        flash('Silakan login terlebih dahulu.', 'error')
        return redirect(url_for('auth.login'))

    # 2. Ambil tenant_id dari session
    tenant_id = get_current_tenant_id()

    # 3. Query + delete dengan FILTER DOUBLE (id + tenant_id)
    session_db = db_manager.get_session()
    try:
        product = session_db.query(Product).filter(
            Product.id == product_id,
            Product.tenant_id == tenant_id,  # ← KUNCI ISOLASI!
        ).first()

        if product is None:
            flash('Produk tidak ditemukan atau bukan milik Anda.', 'error')
            return redirect(url_for('products.list_products'))

        # Simpan nama sebelum delete (untuk flash message)
        product_name = product.name

        # Hapus dari database
        session_db.delete(product)
        session_db.commit()

        flash(f'Produk "{product_name}" berhasil dihapus!', 'success')
        return redirect(url_for('products.list_products'))

    except Exception as e:
        session_db.rollback()
        flash(f'Error: {e}', 'error')
        return redirect(url_for('products.list_products'))
    finally:
        session_db.close()