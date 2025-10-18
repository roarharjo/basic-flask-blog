from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Post
from .markdown_utils import markdown_to_html


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
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('blog.index'))
    return render_template('new.html')


