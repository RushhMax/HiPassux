from flask import Blueprint, jsonify, request
from app.domain.services.reaction_service import ReactionService

reaction_api = Blueprint('reaction_api', 'reaction_api', url_prefix='/api/reactions')

@reaction_api.route('/', methods=['GET'])
def get_reactions():
    reactions = ReactionService.get_all_reactions()
    return jsonify([reaction.to_dict() for reaction in reactions])

@reaction_api.route('/<int:reaction_id>', methods=['GET'])
def get_reaction(reaction_id):
    reaction = ReactionService.get_reaction_by_id(reaction_id)
    if reaction:
        return jsonify(reaction.to_dict())
    return jsonify({'error': 'Reaction not found'}), 404

@reaction_api.route('/', methods=['POST'])
def create_reaction():
    data = request.json
    new_reaction = ReactionService.create_reaction(data)
    return jsonify(new_reaction.to_dict()), 201

@reaction_api.route('/<int:reaction_id>', methods=['PUT'])
def update_reaction(reaction_id):
    data = request.json
    updated_reaction = ReactionService.update_reaction(reaction_id, data)
    if updated_reaction:
        return jsonify(updated_reaction.to_dict())
    return jsonify({'error': 'Reaction not found'}), 404

@reaction_api.route('/<int:reaction_id>', methods=['DELETE'])
def delete_reaction(reaction_id):
    success = ReactionService.delete_reaction(reaction_id)
    if success:
        return jsonify({'message': 'Reaction deleted successfully'})
    return jsonify({'error': 'Reaction not found'}), 404
