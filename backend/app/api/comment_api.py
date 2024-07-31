from flask import Blueprint, jsonify, request
from app.domain.services.comment_service import CommentService

comment_api = Blueprint('comment_api', 'comment_api', url_prefix='/api/comments')

@comment_api.route('/', methods=['GET'])
def get_comments():
    comments = CommentService.get_all_comments()
    return jsonify([comment.to_dict() for comment in comments])

@comment_api.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = CommentService.get_comment_by_id(comment_id)
    if comment:
        return jsonify(comment.to_dict())
    return jsonify({'error': 'Comment not found'}), 404

@comment_api.route('/', methods=['POST'])
def create_comment():
    data = request.json
    new_comment = CommentService.create_comment(data)
    return jsonify(new_comment.to_dict()), 201

@comment_api.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    updated_comment = CommentService.update_comment(comment_id, data)
    if updated_comment:
        return jsonify(updated_comment.to_dict())
    return jsonify({'error': 'Comment not found'}), 404

@comment_api.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    success = CommentService.delete_comment(comment_id)
    if success:
        return jsonify({'message': 'Comment deleted successfully'})
    return jsonify({'error': 'Comment not found'}), 404
