from flask import Blueprint, jsonify, request
from app.domain.services.comment_service import CommentService
from flask_cors import CORS, cross_origin

comment_api = Blueprint('comment_api', 'comment_api', url_prefix='/api/comments')

error_comment = 'Comment not found'

@comment_api.route('/', methods=['GET'])
@cross_origin()
def get_comments():
    comments = CommentService.get_all_comments()
    return jsonify([comment.to_dict() for comment in comments])

@comment_api.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = CommentService.get_comment_by_id(comment_id)
    if comment:
        return jsonify(comment.to_dict())
    return jsonify({'error': error_comment}), 404

@comment_api.route('/', methods=['POST'])
def create_comment():
    data = request.json
    content = data.get('content')
    user_id = data.get('user_id')
    post_id = data.get('post_id')
    
    new_comment = CommentService.create_comment(content, user_id, post_id)
    return jsonify(new_comment.to_dict()), 201

@comment_api.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    content = data.get('content')
    
    updated_comment = CommentService.update_comment(comment_id, content)
    if updated_comment:
        return jsonify(updated_comment.to_dict())
    return jsonify({'error': error_comment}), 404

@comment_api.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    success = CommentService.delete_comment(comment_id)
    if success:
        return jsonify({'message': 'Comment deleted successfully'})
    return jsonify({'error': error_comment}), 404