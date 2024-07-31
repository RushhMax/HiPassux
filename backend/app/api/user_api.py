from flask import Blueprint, jsonify, request
from app.domain.services.user_service import UserService

user_api = Blueprint('user_api', 'user_api', url_prefix='/api/users')

error_User = 'User not found'

@user_api.route('/', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_api.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': error_User}), 404

@user_api.route('/', methods=['POST'])
def create_user():
    data = request.json
    new_user = UserService.create_user( #username, first_name, last_name, birth_date, phone_number, gender, email, password):
        data.get('username'),
        data.get('first_name'),
        data.get('last_name'),
        data.get('birth_date'),
        data.get('phone_number'),
        data.get('gender'),
        data.get('email'),
        data.get('password')
    )
    return jsonify(new_user.to_dict()), 201

@user_api.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_user = UserService.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({'error': error_User}), 404

@user_api.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = UserService.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': error_User}), 404
