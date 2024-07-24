from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.post_service import PostService
from datetime import datetime

bp = Blueprint('post', __name__)

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = PostService.get_all_posts()
    return render_template('posts.html', posts=posts)

@bp.route('/newPost', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        try:
            content = request.form['content']
            author_id = request.form['author_id']  # Assuming you have a way to determine the author

            # Call the PostService to create a new post
            PostService.create_post(
                content=content,
                author_id=author_id
            )

            return redirect(url_for('post.get_posts'))  # Redirect after creating the post

        except Exception as e:
            return render_template('new_post.html', error=f'An error occurred: {e}')
    
    # If GET, just show the form
    return render_template('new_post.html')
