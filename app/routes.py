from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Post, Attachment
from .markdown_utils import markdown_to_html
from .upload_utils import save_upload


bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)


@bp.route('/post/<int:post_id>')
def post_detail(post_id: int):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        body = request.form.get('body', '').strip()
        if not title or not body:
            flash('Title and body are required.', 'error')
            return redirect(url_for('blog.new_post'))
        
        # Process markdown to HTML
        body_html = markdown_to_html(body)
        
        post = Post(title=title, body=body, body_html=body_html, author=current_user)
        db.session.add(post)
        db.session.flush()  # Flush to get post ID before handling uploads
        
        # Handle file uploads
        if 'images' in request.files:
            files = request.files.getlist('images')
            for file in files:
                if file and file.filename != '':
                    result = save_upload(file, post.id)
                    if result:
                        filename, file_path = result
                        attachment = Attachment(filename=filename, file_path=file_path, post=post)
                        db.session.add(attachment)
        
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('blog.index'))
    return render_template('new.html')


