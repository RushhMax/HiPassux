from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.friends_service import FriendRequestService

bp = Blueprint('friend_request', __name__)

@bp.route('/friend_requests', methods=['GET'])
def get_friend_requests():
    result = FriendRequestService.get_all_friend_requests()
    return render_template('friend_requests.html', friend_requests=result['data'])

@bp.route('/friend_requests/send', methods=['POST'])
def send_friend_request():
    sender_username = request.form.get('sender_username')
    receiver_username = request.form.get('receiver_username')
    
    result = FriendRequestService.send_friend_request(sender_username, receiver_username)
    return redirect(url_for('friend_request.get_friend_requests', message=result['message']))

@bp.route('/friend_requests/respond/<int:request_id>', methods=['POST'])
def respond_to_friend_request(request_id):
    action = request.form.get('action')
    result = FriendRequestService.respond_to_friend_request(request_id, action)
    return redirect(url_for('friend_request.get_friend_requests', message=result['message']))
