from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from . import db
from .models import User, Post


bp = Blueprint('admin', __name__)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Login required', 'error')
            return redirect(url_for('auth.login'))
        # Temporarily allow all logged-in users to access admin
        # if not current_user.is_admin:
        #     flash('Admin access required', 'error')
        #     return redirect(url_for('blog.index'))
        return f(*args, **kwargs)
    return decorated_function


@bp.route('/')
@login_required
@admin_required
def dashboard():
    users = User.query.all()
    posts = Post.query.order_by(Post.created_at.desc()).limit(10).all()
    return render_template('admin/dashboard.html', users=users, posts=posts)


@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)


@bp.route('/users/<int:user_id>/toggle-admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('Cannot modify your own admin status', 'error')
        return redirect(url_for('admin.users'))
    user.is_admin = not user.is_admin
    db.session.commit()
    status = 'admin' if user.is_admin else 'user'
    flash(f'{user.username} is now a {status}', 'success')
    return redirect(url_for('admin.users'))


@bp.route('/posts')
@login_required
@admin_required
def posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('admin/posts.html', posts=posts)


@bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = post.title
    db.session.delete(post)
    db.session.commit()
    flash(f'Post "{title}" deleted', 'success')
    return redirect(url_for('admin.posts'))
