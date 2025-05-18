import os
import secrets
from PIL import Image
from flask import current_app

def save_picture(form_picture, folder='profile_pics'):
    """Save a profile or product picture with a random name and return the filename"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    
    # Determine the appropriate subfolder
    if folder == 'profile_pics':
        picture_path = os.path.join(current_app.root_path, 'static/uploads/profile_pics', picture_fn)
        # Resize profile images to save space and load faster
        output_size = (150, 150)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)
    else:  # product_pics
        picture_path = os.path.join(current_app.root_path, 'static/uploads/product_pics', picture_fn)
        # For product images, maintain aspect ratio but limit max size
        max_size = (800, 800)
        i = Image.open(form_picture)
        i.thumbnail(max_size)
        i.save(picture_path)
    
    return picture_fn