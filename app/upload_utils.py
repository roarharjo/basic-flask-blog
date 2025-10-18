"""
File upload utilities for handling image uploads.
"""
import os
import secrets
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


def allowed_file(filename: str) -> bool:
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_upload(file, post_id: int) -> tuple[str, str] | None:
    """
    Save uploaded file securely.
    
    Args:
        file: FileStorage object from request
        post_id: ID of the post
        
    Returns:
        Tuple of (filename, relative_path) or None if invalid
    """
    if not file or file.filename == '':
        return None
    
    if not allowed_file(file.filename):
        return None
    
    if file.content_length > MAX_FILE_SIZE:
        return None
    
    # Create post upload directory
    upload_dir = f'app/static/uploads/{post_id}'
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate secure filename with random suffix
    ext = file.filename.rsplit('.', 1)[1].lower()
    random_name = f"{secrets.token_hex(8)}.{ext}"
    file_path = os.path.join(upload_dir, random_name)
    
    # Save file
    file.save(file_path)
    
    # Return relative path for database storage
    relative_path = f'uploads/{post_id}/{random_name}'
    return file.filename, relative_path
