from flask import Blueprint, jsonify, request
from app.domain.services.message_service import MessageService

message_api = Blueprint('message_api', 'message_api', url_prefix='/api/messages')

@message_api.route('/', methods=['GET'])
def get_messages():
    messages = MessageService.get_all_messages()
    return jsonify([message.to_dict() for message in messages])

@message_api.route('/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = MessageService.get_message_by_id(message_id)
    if message:
        return jsonify(message.to_dict())
    return jsonify({'error': 'Message not found'}), 404

@message_api.route('/', methods=['POST'])
def create_message():
    data = request.json
    new_message = MessageService.create_message(data)
    return jsonify(new_message.to_dict()), 201

@message_api.route('/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    data = request.json
    updated_message = MessageService.update_message(message_id, data)
    if updated_message:
        return jsonify(updated_message.to_dict())
    return jsonify({'error': 'Message not found'}), 404

@message_api.route('/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    success = MessageService.delete_message(message_id)
    if success:
        return jsonify({'message': 'Message deleted successfully'})
    return jsonify({'error': 'Message not found'}), 404
