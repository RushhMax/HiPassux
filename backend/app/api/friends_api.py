from flask import Blueprint, jsonify, request
from app.extensions import db
from app.domain.services.friends_service import FriendRequest, RequestStatus

friend_request_api = Blueprint('friend_request_api', __name__, url_prefix='/api/friend_requests')

@friend_request_api.route('/', methods=['POST'])
def send_friend_request():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')

    if sender_id == receiver_id:
        return jsonify({'error': 'Cannot send a friend request to yourself.'}), 400

    existing_request = FriendRequest.query.filter_by(sender_id=sender_id, receiver_id=receiver_id).first()
    if existing_request:
        return jsonify({'error': 'Friend request already exists.'}), 400

    new_request = FriendRequest(sender_id=sender_id, receiver_id=receiver_id)
    db.session.add(new_request)
    db.session.commit()
    return jsonify(new_request.to_dict()), 201

@friend_request_api.route('/<int:request_id>', methods=['PUT'])
def respond_to_friend_request(request_id):
    data = request.json
    action = data.get('action')

    request_obj = FriendRequest.query.get(request_id)
    if not request_obj:
        return jsonify({'error': 'Friend request not found.'}), 404

    if action == 'accept':
        request_obj.status = RequestStatus.ACCEPTED
    elif action == 'reject':
        request_obj.status = RequestStatus.REJECTED
    else:
        return jsonify({'error': 'Invalid action.'}), 400

    db.session.commit()
    return jsonify(request_obj.to_dict()), 200

@friend_request_api.route('/<int:request_id>', methods=['GET'])
def get_friend_request(request_id):
    request_obj = FriendRequest.query.get(request_id)
    if request_obj:
        return jsonify(request_obj.to_dict())
    return jsonify({'error': 'Friend request not found.'}), 404

@friend_request_api.route('/', methods=['GET'])
def list_friend_requests():
    requests = FriendRequest.query.all()
    return jsonify([request.to_dict() for request in requests])