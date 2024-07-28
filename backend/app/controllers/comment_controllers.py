from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.comment_service import CommentService
from datetime import datetime

bp = Blueprint('comment', __name__)

@bp.route('/comments', methods=['GET'])
def get_comments():
    comments = CommentService.get_all_comments()
    return render_template('comments.html', comments=comments)
