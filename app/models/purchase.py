from datetime import datetime
from app import db

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    shipping_address = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, shipped, delivered, cancelled
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    items = db.relationship('PurchaseItem', backref='purchase', lazy=True)
    
    def __repr__(self):
        return f"Purchase(ID: {self.id}, Amount: ${self.total_amount}, Status: {self.status})"

class PurchaseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_price = db.Column(db.Float, nullable=False)
    
    # Foreign Keys
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    
    def __repr__(self):
        return f"PurchaseItem(Purchase ID: {self.purchase_id}, Product ID: {self.product_id}, Price: ${self.purchase_price})"