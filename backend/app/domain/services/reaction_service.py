from app.domain.repositories.reaction_repository import Reaction,ReactionRepository

class ReactionService:

    @staticmethod
    def get_all_reactions():
        return ReactionRepository.get_all_Reactions()

    @staticmethod
    def create_reaction(post_id, user_id, comment_id, type):
        new_reaction = Reaction(
            post_id = post_id,
            user_id = user_id,
            comment_id = comment_id,
            type = type
        )
        ReactionRepository.add_Reaction(new_reaction)