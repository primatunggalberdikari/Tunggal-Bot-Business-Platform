"""
Koneksi database menggunakan SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path

from config.settings import settings
from models.base import Base


class DatabaseManager:
    """
    Manager untuk koneksi database.
    Menggunakan pattern Singleton agar hanya ada satu koneksi.
    """
    
    _instance = None
    _engine = None
    _session_local = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._engine is None:
            self._init_engine()
    
    def _init_engine(self) -> None:
        """Inisialisasi engine database."""
        database_url = settings.DATABASE_URL
        
        # Buat folder database jika belum ada
        if database_url.startswith('sqlite:///'):
            db_path = database_url.replace('sqlite:///', '')
            db_dir = Path(db_path).parent
            db_dir.mkdir(parents=True, exist_ok=True)
        
        self._engine = create_engine(
            database_url,
            echo=settings.DEBUG,
            connect_args={"check_same_thread": False} if 'sqlite' in database_url else {}
        )
        self._session_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine
        )
    
    def get_session(self) -> Session:
        """Mendapatkan session database."""
        if self._session_local is None:
            self._init_engine()
        return self._session_local()
    
    def create_tables(self) -> None:
        """Membuat semua tabel di database."""
        if self._engine is None:
            self._init_engine()
        Base.metadata.create_all(bind=self._engine)
    
    def drop_tables(self) -> None:
        """Menghapus semua tabel (untuk testing)."""
        if self._engine is None:
            self._init_engine()
        Base.metadata.drop_all(bind=self._engine)


# Instance global untuk digunakan di seluruh aplikasi
db_manager = DatabaseManager()