from flask import Blueprint, jsonify, request
from app.domain.services.friends_service import FriendRequestService

friend_request_api = Blueprint('friend_request_api', __name__, url_prefix='/api/friend_requests')

error_request = 'Request not found'

@friend_request_api.route('/', methods=['POST'])
def send_friend_request():
    data = request.json
    sender_username = data.get('sender_username')
    receiver_username = data.get('receiver_username')

    result = FriendRequestService.send_friend_request(sender_username, receiver_username)
    if not result['success']:  # Error message
        return jsonify({'error': result['message']}), 400
    return jsonify(result['data']), 201

@friend_request_api.route('/<int:request_id>', methods=['PUT'])
def respond_to_friend_request(request_id):
    data = request.json
    action = data.get('action')

    result = FriendRequestService.respond_to_friend_request(request_id, action)
    if not result['success']:  # Error message
        return jsonify({'error': result['message']}), 400
    return jsonify(result['data']), 200

@friend_request_api.route('/<int:request_id>', methods=['GET'])
def get_friend_request(request_id):
    request_obj = FriendRequestService.get_all_friend_requests()
    request_obj = next((req for req in request_obj['data'] if req['id'] == request_id), None)
    if request_obj:
        return jsonify(request_obj)
    return jsonify({'error': error_request}), 404

@friend_request_api.route('/', methods=['GET'])
def list_friend_requests():
    result = FriendRequestService.get_all_friend_requests()
    return jsonify(result['data'])