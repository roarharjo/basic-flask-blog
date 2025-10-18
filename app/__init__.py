from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    db_path = os.environ.get('DATABASE_URL', 'sqlite:///data/blog.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register blueprints/routes
    from .routes import bp as blog_bp
    app.register_blueprint(blog_bp)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from .admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Create SQLite file/directories on first run (when using sqlite and URI like sqlite:///data/blog.db)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite:///'):
        # Ensure the directory exists
        path_part = app.config['SQLALCHEMY_DATABASE_URI'].split('sqlite:///')[1]
        dir_name = os.path.dirname(path_part)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

    with app.app_context():
        from . import models  # noqa: F401 - ensure models are registered
        db.create_all()
        
        # Create admin user if it doesn't exist
        create_admin_user()

    return app


def create_admin_user():
    """Create an admin user if none exists"""
    from .models import User
    from werkzeug.security import generate_password_hash
    
    # Check if any admin users exist
    admin_exists = User.query.filter_by(is_admin=True).first()
    
    if not admin_exists:
        # Create default admin user
        admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        
        admin_user = User(
            username=admin_username,
            password_hash=generate_password_hash(admin_password),
            is_admin=True
        )
        
        db.session.add(admin_user)
        db.session.commit()
        
        print(f"✅ Admin user created: {admin_username}")
        print(f"🔑 Default password: {admin_password}")
        print("⚠️  Please change the admin password after first login!")
    else:
        print("ℹ️  Admin user already exists")


