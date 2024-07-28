from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.message_service import MessageService
from datetime import datetime

bp = Blueprint('message', __name__)

@bp.route('/messages', methods=['GET'])
def get_messages():
    messages = MessageService.get_all_messages()
    return render_template('messages.html', messages=messages)
