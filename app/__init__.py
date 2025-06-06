from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
import os

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
setattr(login_manager, 'login_view', 'auth.login')
login_manager.login_message_category = 'info'
migrate = Migrate()

def create_app(config_class=Config):
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Ensure the upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.products import products
    app.register_blueprint(products)

    from app.routes.user import user
    app.register_blueprint(user)

    from app.routes.cart import cart
    app.register_blueprint(cart)

    # Create database tables if they don't exist
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from app.models.category import Category
        from app.models.user import User
        from app.models.product import Product
        from app.models.cart import CartItem
        from app.models.purchase import Purchase
        
        # Create all database tables
        db.create_all()
        
        # Import and run setup utilities after tables are created
        from app.models.db_utils import create_default_categories, create_upload_folders
        create_default_categories()
        create_upload_folders()

    return app