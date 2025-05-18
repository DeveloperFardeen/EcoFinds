from datetime import datetime
from app import db
import json

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(20), nullable=False)  # New, Like New, Good, Fair, etc.
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    images = db.Column(db.String(300), nullable=False, default='default_product.jpg')  # Store as JSON string of image filenames
    is_sold = db.Column(db.Boolean, default=False)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    # Relationships
    cart_items = db.relationship('CartItem', backref='product', lazy=True)
    purchase_items = db.relationship('PurchaseItem', backref='product', lazy=True)
    
    def __repr__(self):
        return f"Product('{self.title}', ${self.price}, '{self.condition}')"
    
    def get_images_list(self):
        """Convert the JSON string of images to a list"""
        if self.images == 'default_product.jpg':
            return ['default_product.jpg']
        return json.loads(self.images)
    
    def set_images_list(self, images_list):
        """Convert a list of images to a JSON string"""
        self.images = json.dumps(images_list)