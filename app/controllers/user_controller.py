from flask import Blueprint, render_template, flash, redirect , url_for
from app.domain.services.user_service import UserService

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)
