"""
Modul Web Dashboard untuk Tunggal Bot Business Platform.
"""

from flask import Flask
from config.settings import settings


def create_app() -> Flask:
    """
    Factory function untuk membuat Flask app.
    
    Returns:
        Flask: Instance aplikasi Flask.
    """
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static',
    )
    
    # Konfigurasi
    app.config['SECRET_KEY'] = settings.FLASK_SECRET_KEY or 'dev-secret-key-change-in-production'
    app.config['DEBUG'] = settings.DEBUG
    
     # Register blueprint
    from web.routes.main import main_bp
    from web.routes.auth import auth_bp       
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)          
    
    return app