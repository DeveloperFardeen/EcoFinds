from flask import current_app
from app import db
from app.models import Category
import os

def create_default_categories():
    """Create default categories if they don't exist"""
    default_categories = [
        {'name': 'Clothing', 'description': 'Gently used clothing items for all ages'},
        {'name': 'Electronics', 'description': 'Second-hand electronics in working condition'},
        {'name': 'Furniture', 'description': 'Used furniture for home and office'},
        {'name': 'Books', 'description': 'Used books, textbooks, and literature'},
        {'name': 'Home & Garden', 'description': 'Items for your home and garden'},
        {'name': 'Sports & Outdoors', 'description': 'Used sports equipment and outdoor gear'},
        {'name': 'Toys & Games', 'description': 'Second-hand toys and games'},
        {'name': 'Jewelry & Accessories', 'description': 'Pre-owned jewelry and accessories'},
        {'name': 'Art & Collectibles', 'description': 'Collectible items and artwork'},
        {'name': 'Other', 'description': 'Miscellaneous items that don\'t fit other categories'}
    ]
    
    for category_data in default_categories:
        existing_category = Category.query.filter_by(name=category_data.get('name')).first()
        if not existing_category:
            category = Category(**category_data)
            db.session.add(category)
    
    db.session.commit()
    current_app.logger.info('Default categories created')

def create_upload_folders():
    """Create folders for file uploads"""
    upload_folder = current_app.config['UPLOAD_FOLDER']
    profile_folder = os.path.join(upload_folder, 'profile_pics')
    product_folder = os.path.join(upload_folder, 'product_pics')
    
    os.makedirs(profile_folder, exist_ok=True)
    os.makedirs(product_folder, exist_ok=True)
    current_app.logger.info('Upload folders created')