from datetime import datetime
from app import db

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    
    def __repr__(self):
        return f"CartItem(Product ID: {self.product_id}, User ID: {self.user_id})"