from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.comment_service import CommentService
from datetime import datetime

bp = Blueprint('comment', __name__)

commentsGetComments = 'comment.get_comments'

@bp.route('/comments', methods=['GET'])
def get_comments():
    comments = CommentService.get_all_comments()
    return render_template('comments.html', comments=comments)

@bp.route('/comments/create', methods=['POST'])
def create_comment():
    content = request.form.get('content')
    user_id = request.form.get('user_id')
    post_id = request.form.get('post_id')

    CommentService.create_comment(content, user_id, post_id)
    return redirect(url_for(commentsGetComments))

@bp.route('/comments/update/<int:comment_id>', methods=['POST'])
def update_comment(comment_id):
    content = request.form.get('content')

    CommentService.update_comment(comment_id, content)
    return redirect(url_for(commentsGetComments))

@bp.route('/comments/delete/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    CommentService.delete_comment(comment_id)
    return redirect(url_for(commentsGetComments))