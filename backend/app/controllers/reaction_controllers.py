from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.reaction_service import ReactionService
from datetime import datetime

bp = Blueprint('reaction', __name__)

@bp.route('/reactions', methods=['GET'])
def get_reactions():
    reactions = ReactionService.get_all_reactions()
    return render_template('reactions.html', reactions=reactions)
