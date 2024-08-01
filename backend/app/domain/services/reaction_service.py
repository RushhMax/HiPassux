from app.domain.repositories.reaction_repository import Reaction,ReactionRepository

reactionNF = 'Reaccion no encontrada'

class ReactionService:

    @staticmethod
    def get_all_reactions():
        return ReactionRepository.get_all_reactions()

    @staticmethod
    def get_reactions_by_post(post_id):
        return ReactionRepository.get_reactions_by_post(post_id)

    @staticmethod
    def get_reactions_by_comment(comment_id):
        return ReactionRepository.get_reactions_by_comment(comment_id)

    @staticmethod
    def create_reaction(user_id, type,post_id=None, comment_id=None):
        new_reaction = Reaction(
            post_id = post_id,
            user_id = user_id,
            comment_id = comment_id,
            type = type
        )
        ReactionRepository.add(new_reaction)
        return new_reaction
    
    @staticmethod
    def update_reaction_by_post_and_user(post_id, user_id, data):
        reaction = ReactionRepository.get_reaction_by_post_and_user(post_id, user_id)

        if not reaction:
            return None, reactionNF
        
        reaction.type = data.get('type', reaction.type)

        ReactionRepository.update_reaction(reaction)
        return reaction, None
    
    @staticmethod
    def update_reaction_by_comment_and_user(comment_id, user_id, data):
        reaction = ReactionRepository.get_reaction_by_comment_and_user(comment_id, user_id)

        if not reaction:
            return None, reactionNF
        
        reaction.type = data.get('type', reaction.type)

        ReactionRepository.update_reaction(reaction)
        return reaction, None
        
    @staticmethod
    def delete_reaction_by_post_and_user(post_id, user_id):
        reaction = ReactionRepository.get_reaction_by_post_and_user(post_id, user_id)

        if not reaction:
            return False, reactionNF

        ReactionRepository.delete_reaction(reaction)
        return True, None

    @staticmethod
    def delete_reaction_by_comment_and_user(comment_id, user_id):
        reaction = ReactionRepository.get_reaction_by_comment_and_user(comment_id, user_id)

        if not reaction:
            return False, reactionNF

        ReactionRepository.delete_reaction(reaction)
        return True, None