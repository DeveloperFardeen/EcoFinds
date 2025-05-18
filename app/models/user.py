from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from flask import current_app
import os
import secrets

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    bio = db.Column(db.Text)
    location = db.Column(db.String(100))
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    products = db.relationship('Product', backref='seller', lazy=True)
    purchases = db.relationship('Purchase', backref='buyer', lazy=True)
    cart_items = db.relationship('CartItem', backref='user', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"